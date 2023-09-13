import tkinter as tk
import sounddevice as sd
import wavio

class VoiceRecorderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.is_recording = False
        self.frames = []

        self.setup_ui()

    def setup_ui(self):
        self.record_button = tk.Button(self.root, text="Record", command=self.toggle_record)
        self.record_button.pack(pady=20)

        self.save_button = tk.Button(self.root, text="Save Recording", command=self.save_recording, state=tk.DISABLED)
        self.save_button.pack(pady=10)

    def toggle_record(self):
        if not self.is_recording:
            self.record_button.config(text="Stop Recording")
            self.is_recording = True
            self.start_recording()
        else:
            self.record_button.config(text="Record")
            self.is_recording = False
            self.stop_recording()
            self.save_button.config(state=tk.NORMAL)

    def start_recording(self):
        self.frames = []
        print("Recording...")
        sd.default.samplerate = 44100
        sd.default.channels = 2

        def callback(indata, frames, time, status):
            if status:
                print(status)
            self.frames.append(indata.copy())

        self.stream = sd.InputStream(callback=callback)
        self.stream.start()

    def stop_recording(self):
        print("Recording stopped.")
        self.stream.stop()

    def save_recording(self):
        filename = "recorded_audio.wav"
        wavio.write(filename, self.frames, 44100, sampwidth=2)
        print(f"Recording saved as {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderGUI(root)
    root.mainloop()

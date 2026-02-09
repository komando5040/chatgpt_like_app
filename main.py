from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class ChatLayout(BoxLayout):
    chat_history = StringProperty("")

    def send_message(self, user_text):
        if not user_text.strip():
            return

        self.chat_history += f"شما: {user_text}\n"

        response = self.bot_response(user_text)
        self.chat_history += f"بات: {response}\n\n"

        self.ids.user_input.text = ""

    def bot_response(self, text):
        text = text.lower()

        if "سلام" in text:
            return "سلام! حالت چطوره؟ 😊"
        elif "خوبی" in text:
            return "ممنون، خوبم! تو چطوری؟"
        elif "اسمت" in text:
            return "من یه چت‌بات ساده‌ام 🤖"
        else:
            return "فعلاً فقط سلام و احوال‌پرسی بلدم 🙂"


class ChatApp(App):
    def build(self):
        return ChatLayout()


if __name__ == "__main__":
    ChatApp().run()

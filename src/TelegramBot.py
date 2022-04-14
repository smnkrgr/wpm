from src.Event import Event
import telegram
import random


class TelegramBot():

    def __init__(self, token, chat_id) -> None:
        # Create the bot API wrapper
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat_id

        # Donger disposal
        self.donger_list = [
                "ԅ(☉Д☉)╮", "⊂(▀¯▀⊂)", "(✿ ◕‿◕) ᓄ✂╰U╯",
                "(ʘ言ʘ╬)", "(ʘᗩʘ’)", "༼⁰o⁰；༽",
                "ԅ⁞ ◑ ₒ ◑ ⁞ᓄ", "╰། ◉ ◯ ◉ །╯", "⋋| ◉ ͟ʖ ◉ |⋌",
                "〳 ͡° Ĺ̯ ͡° 〵", "(っ ºДº)っ ︵ ⌨", "(╯°□°）╯︵ ส็็็็็็็ส"]

    def format_and_send_new_pb(self, pb, name) -> None:
        message = self._format_message(pb, name)
        self._send_message(message)

    def get_random_donger(self) -> str:
        return random.choice(self.donger_list)


    def _send_message(self, message) -> None:
        Event("Sending PB via Telegram")
        try:
            self.bot.send_message(text=message, chat_id=self.chat_id)
            Event("Message sent!", is_success=True)
        except Exception as e:
            message = "Sending the telegram messeage went wrong: " + str(e)
            Event(message, is_error=True, exit=True)

    def _format_message(self, pb, name) -> str:
        # Extract information from the pb if present
        wpm = "" if not 'wpm' in pb else str(pb['wpm'])
        acc = "" if not 'acc' in pb else str(pb['acc'])
        mode = "" if not 'mode' in pb else str(pb['mode']).capitalize()
        mode2 = "" if not 'mode2' in pb else str(pb['mode2'])
        diff = "Standard" if not 'difficulty' in pb else str(pb['difficulty'])
        lang = "English" if not 'language' in pb else str(pb['language']).capitalize()
        consist = "" if not 'consistency' in pb else str(pb['consistency'])
        # Construct the message
        donger = self.get_random_donger()
        message = name + "  " + donger +"\n"
        message += "New PB for mode: "+mode+" ("+lang+", "+mode2+"s, "+diff+")\n"
        message += "WPM: "+wpm+" (Accuracy: "+acc+"%, Consistency: "+consist+"%)"
        return message



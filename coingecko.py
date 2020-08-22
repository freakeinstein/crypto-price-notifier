from pycoingecko import CoinGeckoAPI
import numpy as np
import time
import vlc

cg = CoinGeckoAPI()

positive_player = vlc.MediaPlayer("sounds/8d82b5_Angry_Birds_Star_Collect_Sound_Effect.mp3")
negative_player = vlc.MediaPlayer("sounds/8d82b5_Angry_Birds_TNT_Sound_Effect.mp3")
all_good_player = vlc.MediaPlayer("sounds/8d82b5_Angry_Birds_Golden_Egg_Sound_Effect.mp3")
no_change_player = vlc.MediaPlayer("sounds/8d82b5_Angry_Birds_Bird_Destroyed_Sound_Effect.mp3")

class gecko:

    def __init__(self, interested_coins):
        self.interested_coins = interested_coins
        self.old_values = [0.0] * len(interested_coins)

    def price_info_usd (self):
        prices = cg.get_price(ids=self.interested_coins, vs_currencies=["usd"])

        ret = []
        for coin in self.interested_coins:
            ret.append(prices[coin]["usd"])

        return ret


    def find_change (self):
        current_values = self.price_info_usd()

        diff = np.subtract(np.array(current_values), np.array(self.old_values))

        self.old_values = current_values

        return diff.tolist()

    def generate_reports (self):
        changes = self.find_change()

        # generate sounds
        sound_array = []
        for change in changes:
            if change < 0:
                sound_array.append(-100)
            elif change > 0:
                sound_array.append(1000)
            else:
                sound_array.append(0)
        
        sound_sum = np.sum(np.array(sound_array))
        if sound_sum == len(changes)*1000:
            all_good_player.play()
            time.sleep(2)
            all_good_player.stop()
        elif sound_sum == 0:
            no_change_player.play()
            time.sleep(2)
            no_change_player.stop()
        else:
            for sound in sound_array:
                if sound < 0:
                    negative_player.play()
                    time.sleep(1)
                    negative_player.stop()
                if sound == 0:
                    no_change_player.play()
                    time.sleep(2)
                    no_change_player.stop()
                if sound > 0:
                    positive_player.play()
                    time.sleep(1)
                    positive_player.stop()

        return (changes)
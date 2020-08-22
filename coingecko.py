from pycoingecko import CoinGeckoAPI
import numpy as np
import time
import vlc

cg = CoinGeckoAPI()

positive_player = vlc.MediaPlayer("sounds/8d82b5_Angry_Birds_Star_Collect_Sound_Effect.mp3")
negative_player = vlc.MediaPlayer("sounds/8d82b5_Angry_Birds_TNT_Sound_Effect.mp3")
all_good_player = vlc.MediaPlayer("sounds/8d82b5_Angry_Birds_Golden_Egg_Sound_Effect.mp3")
no_change_player = vlc.MediaPlayer("sounds/8d82b5_Angry_Birds_Bird_Destroyed_Sound_Effect.mp3")
all_down_player = vlc.MediaPlayer("sounds/super-mario-death-sound-sound-effect.mp3")

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

        return current_values, diff.tolist()

    def generate_reports (self):
        current_values, changes = self.find_change()
        all_down = True
        all_up = True
        all_meh = True

        # generate sounds
        sound_array = []
        for change in changes:
            if change < 0:
                sound_array.append(-1)
                all_up = False
                all_meh = False
            elif change > 0:
                sound_array.append(1)
                all_down = False
                all_meh = False
            else:
                sound_array.append(0)
                all_up = False
                all_down = False
        
        if all_up:
            all_good_player.play()
            time.sleep(2)
            all_good_player.stop()
            print("=== All coins are bullish ====")
        elif all_meh:
            no_change_player.play()
            time.sleep(2)
            no_change_player.stop()
            print("=== All coins are sideways ====")
        elif all_down:
            all_down_player.play()
            time.sleep(2)
            all_down_player.stop()
            print("=== All coins are bearish ====")
        else:
            for idx, sound in enumerate(sound_array):
                if sound < 0:
                    negative_player.play()
                    print("=== "+self.interested_coins[idx]+" is bearish. "+str(current_values[idx])+" - "+str(changes[idx]*-1)+" ====")
                    time.sleep(1)
                    negative_player.stop()
                if sound == 0:
                    no_change_player.play()
                    print("=== "+self.interested_coins[idx]+" is sideways. "+str(current_values[idx])+" ====")
                    time.sleep(2)
                    no_change_player.stop()
                if sound > 0:
                    positive_player.play()
                    print("=== "+self.interested_coins[idx]+" is bullish. "+str(current_values[idx])+" + "+str(changes[idx])+" ====")
                    time.sleep(1)
                    positive_player.stop()

        return current_values, changes
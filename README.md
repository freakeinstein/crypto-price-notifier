# crypto-price-notifier
Get audio notification when bitcoin ethereum any crypto currency goes down or up. Just like Gilfoyle's Bitcoin Warning in Silicon Valley series.

![respect](https://thumbs.gfycat.com/SlimyBeneficialBassethound-max-1mb.gif)

##### Prerequisite
You need VLC player installed in your system
Also run these commands:
```
pip install pycoingecko
pip install python-vlc
```
### Run Notifier
`python server.py <timeout in seconds> <coin1 name> <coin2 name> ...`

for example, `python server.py 3600 bitcoin ethereum chainlink ocean-protocol`

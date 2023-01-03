# wows_client
## under construction
## Usage
```py
import wows
app=wows.App(application_id,"en")
app.get_player("")
```
### App
`application_id`:str: literal

`lang`:str: your language (country code)

`conv`:bool:
If `True` passed,convert dictionary to `convdict.Dict`.

You can use like this.
```py
get_ship("yamato").origin
>>>{"name":"yamato","details":{"some":"aaaa"}}
get_ship("yamato").value.details.some
>>>aaaa
```
Default is `False`.

#### get_user
:return: Player object

You can get original returned dict from WGapi by `get_user.origin`
#### get_ship
:return: Ship object

same
#### get_arena
:return: Arena object

same
### Player
#### generate_figure
:return: None

`path`:str: save path

generate graph of player’s nations and ship types.It may took few seconds to generate.


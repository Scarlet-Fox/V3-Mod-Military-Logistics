# Military Logistics and Stockpiles (Victoria 3 Mod)

This mod adds features to the game for stockpiling and distributing strategic goods for your military. This allows you (and the AI) to improve economic stability during warfare, and plan your wars with a more strategic lens.

## Overview (this is the TLDR)

Build a **military logistics center** in a state to start gathering goods for your local strategic reserve. When war starts, **distribution centers** will open in states with a logistics center. These will distribute your reserve into the local market. When war ends, the distribution centers close.

In addition to stockpiling goods, logistics centers will provide your country with additional bureaucracy points and, when they're setup as military academies, they provide some amount of innovation and improved qualifications (training) for your pops.

AI players will build logistics centers, and the centers improve the AI effectiveness. Great powers build logistics centers most frequently, but I've seen smaller nations build them sometimes as well.

This is a lightweight mod that does not dramatically change game performance. It should also be compatible with any mods that don't make dramatic changes to the type of goods used by military units. (Yes, it works with VTM!)

Keep reading for more details, or you can scroll down to the bottom for information on compatibility, known issues, and other mods that I recommend.

## Why Stockpiles?

The base game does not have a stockpiling mechanic. However, the storage of military goods was extremely (and increasingly) important during this time in history. The game's economic model is incomplete without this mod.

As I played Victoria 3 more and more, I realized that something seemed wrong. The autonomous construction queue never seemed to favor building military buildings during peacetime, but wartime was far too late to start building up military industrial buildings. I had to build it myself and subsidize it or it didn't exist.

Additionally, AI players, especially great powers, would have the same issue. Since I can't help them with building up their army, it made beating them in warfare fairly trivial. I would just need to stall for time and they typically go bankrupt due to not being able to scale up military industry fast enough to make military goods cheaper.

This is not realistic. It bothered me. For one thing, subsidizing my military industry during peacetime is fine, but all of the guns and ammunition that resulted from this just vanished. It was gone into thin air! It made no sense.

I made this mod because the lack of stockpiles really bothered me, and it's bothering you too, even if you don't realize it. With this mod, there is peacetime demand for military goods; the economic impact of war is more controlled; and the AI tends to go bankrupt a bit less when fielding large armies.

## More Details

This mod adds two new building types - Military Logistics Centers and Distribution Centers. Each month, the script will check to see if a military logistics center exists. If it does, then it will increase the stockpiled amounts based on the options that you've selected, the building level, and the employment ratio.

If you are at war, then Distribution Centers open. Each distribution center only distributes a single good, and you have some control over the amount of the distribution. Each month, for each distribution center, the stockpile is decreased based on the options that you've selected and the size and employment of the logistics center. Distribution centers use "minting" to offset the cost of the good (so you don't pay twice).

Stockpiles exist at a state level. I am not in support of country-level stockpiles, because the game developers have said that they will eventually add military supply chain effects back into the game (they were removed during the military rework). When that happens, it will make this mod more interesting if your stockpiled goods have to be transported to the frontlines from the stockpiles.

The AI fully benefits from the mod. They open logistics centers, when they can afford them, in states where this seems to make sense. They toggle the options on the buildings in a way that improves their military supplies. I'm satisfied with how this works, given the limits of the game engine.

The recent addition of local goods prices works very well with this mod. Just build your logistics centers where your major military production occurs and you can buy goods a bit cheaper than you could otherwise.

## Is It Balanced?

I welcome feedback on this, but I'd say it's pretty balanced. Stockpiles are capped in size. Stockpiling military goods isn't free (and isn't too expensive). I used a spreadsheet to figure everything out so that it all made sense. It seems to work quite nicely when I played the game with it. Give it a try, let me know your thoughts.

Please note, stockpiles make the game more pleasant to play, they don't necessarily make the game easier or more difficult. 

Great powers and other AI countries with large amounts of wealth end up with stronger military industries, which means their armies can be more dangerous to engage with. This is working as intended, and it makes the game flow much better in my opinion.

Players can leverage stockpiles to plan their wars more effectively. 

## Lore

> “Infantry wins battles, logistics wins wars.”
>
> -- John Pershing, US Army General

Prior to the [Napoleonic Wars (1803 - 1815)](https://en.wikipedia.org/wiki/Napoleonic_Wars), armies were typically supplied by taking supplies from the surrounding area. This "local supply" worked because military supplies were simple and army objectives were often populated areas.

Local supplies also worked because pre-industrial era armies were typically smaller than modern armies. However, as armies grew larger and military technology advanced, local supplies were no longer sufficient. Put another way, there was no way to supply more than a hundred thousand men with bullets by scavenging the countryside.

Industrial era technologies like railways, canning, refrigeration, and steam-powered ships dramatically improved the ability to move army supplies. As military supply operations became increasingly complex, specialized professionals became necessary to oversee the purchase, storage, transport, and preservation of these supplies.

Military Logistics grew from this increasing complexity. In modern warfare, the ability to get supplies to your army really can make the difference between winning and losing a war. Local supplies really aren't a thing anymore. This is a change that occurred during the timeline covered by Victoria 3.

## Multiplayer Compatibility

I don't have any friends to play Victoria 3 multiplayer with, and I'm not even sure multiplayer is for me. This means that I don't know if this mod works in multiplayer or not. Give it a try! Let me know if it works!

## Mod Compatibility

I wanted as many players to be able to use this mod as possible, so this mod has been made to avoid conflicts with other mods. Most mods should work with this one just fine. 

### Compatibility Details

The only file from the base game that is modified is the "building_details_panel.gui" file, which is where the stockpile display has been added to the logistics center. If that file is overridden by another mod, then you can't see stockpile levels, which is not that big of a deal to be honest. So, even if there is a conflict, load other mods over this one and the conflict will be resolved.

## Known Issues

* There is some ugliness in the stockpiles interface. I don't know why it happens, and nothing I tried seems to resolve it.
* If you take a state with a stockpile in it, you get the stockpile. I am still thinking about what to do about this (if anything).

## Potential Future Additions

I'm not sure. Apparently, the game developers are considering adding stockpiles themselves. We'll have to see what the future holds. If you have any ideas, let me know.

## Contributions Appreciated!!!

Give me your feedback! I appreciate it! Just keep in mind that I may not change the mod based on feedback that I've recieved.

Language translations are always welcome! 

Finally, there is an open source repository that you can interact with if you would like to contribute.

## Special Thanks!

* This mod uses code from the [multi-line production methods framework](https://github.com/1230james/vic3-multi-line-pms-framework), which was created by [1230james](https://github.com/1230james). Thank you 1230james!
* The korean language translation was provided by [dungsil](https://github.com/dungsil). Thank you dungsil!

## Other Mods I Use

* [Victoria Tweaks Mod](https://steamcommunity.com/sharedfiles/filedetails/?id=2935989855)
* [Forts and Engineers](https://steamcommunity.com/sharedfiles/filedetails/?id=3005432154)
* [Locomotion: Land, Water, & Air](https://steamcommunity.com/sharedfiles/filedetails/?id=3032533792)
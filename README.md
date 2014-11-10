Spellimobulator
==

A program that, given AP, AD, and CDR values, calculates the most 'efficient' activated spell in the game League of Legends.

The 'efficiency' of a spell is going to be interpreted as the damage per second that spell can inflict to a single target.

DPS is calculated by taking the amount of damage the spell does to one target, and dividing it by its cooldown. This means no other abilities or previously activated spells are taken into consideration. Things like Karma and Leblanc's Ultimates will be calculated separately as special condition abilities.

This does mean that channeled spells have somewhat of an advantage, but in terms of efficiency, this is a proper conclusion.

This program may be improved on with later iterations to take more variables into consideration.

## Known Inaccuracies

* Any spell that calculates damage based on % AD rather than Flat AD will be calculated as if it were Flat AD since no discretion between the two is available.
* All spell damage is calculated as if it affects only 1 target. For example, Brand's Pyroclasm will only bounce once.
* Spells that do not directly inflict damage are not being considered as damaging spells. i.e., Attack modifiers and "Every 3rd attack does X damage" are not being considered as Attack Speed is unknown.
* Spells that deal extra damage based on variables that are not AD or AP will not have that extra damage taken into consideration.
* Costs would normally be considered when calculating 'efficiency', but many spells have no costs, or use some other type of self regenerating cost type. So, spell costs are being left out for now to provide a more fair analysis.
* All spells are being calculated at maximum level.
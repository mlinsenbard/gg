Spellimobulator
==

A program that, given AP, AD, and CDR values, calculates the most 'efficient' activated spell in the game League of Legends.

The 'efficiency' of a spell is going to be interpreted as the damage per second that spell can inflict to a single target champion.

DPS is calculated by taking the amount of damage the spell does to one target, and dividing it by its cooldown. This means no other abilities or previously activated spells are taken into consideration. Things like Karma's and Leblanc's Ultimates will be calculated separately as special condition abilities.

This does mean that channeled or toggled spells have somewhat of an advantage, but in reality Kog'Maw reigns champion, it seems.

## Known Inaccuracies

* Mana costs are not taken into consideration for 'efficiency'. This is because spells with no cost, energy costs, and health costs would have an unfair advantage.
* Bonus AD and Flat AD are the same since no discretion can be made given 1 value for AD.
* All spell damage is calculated as if it affects only 1 target. For example, Brand's Pyroclasm will only bounce once.
* Spells that do not directly inflict damage are not being considered as damaging spells. i.e., Attack modifiers and "Every 3rd attack does X damage" are not being considered as Attack Speed is unknown.
* Spells that deal extra damage based on variables that are not AD or AP will not have that extra damage taken into consideration.
* Costs would normally be considered when calculating 'efficiency', but many spells have no costs, or use some other type of self regenerating cost type. So, spell costs are being left out for now to provide a more fair analysis.
* All spells are being calculated at maximum level.
gg
==

A program that, given AP, AD, and CDR values, calculates the most 'efficient' spell in the game League of Legends.
The 'efficiency' of a spell is going to be interpreted as the damage per second that spell can inflict to a single target.

The highest CD spell of 180s (Karthus' lvl1 Ult) will be used as a baseline for calculating the DPS of all other spells.

This program may be improved on with later iterations to take more variables into consideration.

## Known Inaccuracies

* Any spell that calculates damage based on % AD rather than Flat AD will be calculated as if it were Flat AD since no discretion between the two is available.
* All spell damage is calculated as if it affects only 1 target. For example, Brand's Pyroclasm will only bounce once.
* Spells that do not directly inflict damage are not being considered as damaging spells. i.e. Abilities lacking a label of "Damage" are not considered.
* Spells that deal % HP damage will be calculated as if the target and host have 2000HP.
* Costs would normally be considered when calculating 'efficiency', but many spells have no costs, or use some other type of self regenerating cost type. So, spell costs are being left out for now.
* All spells are being calculated at maximum level.
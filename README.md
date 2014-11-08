gg
==

A program that, given AP, AD, and CDR values, calculates the most 'efficient' spell in the game League of Legends.
The 'efficiency' of a spell is going to be interpreted as the damage per second that spell can inflict to a single target.

The highest CD spell of 180s (Karthus' lvl1 Ult) will be used as a baseline for calculating the DPS of all other spells.

Later iterations of this program may attempt to offer more accuracies in terms of using the champions' default HP/AD/ARMR/MR/AS values 
when calculating spell damage.

## Known Inaccuracies

* Any spell that calculates damage based on % AD rather than Flat AD will be calculated as if it were Flat AD.
* All spell damage is calculated as if it affects only 1 target. (For example, Brand's Pyroclasm will only hit once.)
* Spells that increase attack damage or attack speed are not being considered as damaging spells.
* Spells that deal % HP damage will be calculated as if the target and host have 2000HP.

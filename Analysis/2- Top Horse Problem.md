# You have given 25 horses and have to find top 3 in minimum races.Only five horses can participate in a race.

To find the top 3 horses among 25 with a constraint of only 5 horses racing at a time, you can use the following approach:

### Initial Races (5 races):
- Divide the 25 horses into 5 groups of 5 horses each.
- Conduct 5 races with each group, determining the fastest horse in each group.

### Overall Ranking (Initial Ranking):
- Combine the winners of each group race into a new race (Race 6).
- The winner of this race is the overall fastest horse.
- The second and third positions in this race are the second and third fastest horses overall.

### Additional Races for Ranking:
- Now, you have the top 3 horses from Race 6, and you also have the winners of the remaining 4 groups (not included in the initial 6-race process).
- Conduct two additional races (Races 7 and 8):
> - Race 7: Winners of the 2nd positions from the initial group races, the 2nd position horse from the overall ranking (Race 6).
> - Race 8: Winners of the 3rd positions from the initial group races, the 3rd position horse from the overall ranking (Race 6).
- This will give you the order of the 2nd and 3rd position horses overall.

### Final Ranking:
- The winner of Race 6 is the fastest horse.
- The 2nd and 3rd position horses from Race 7 and Race 8 are the 2nd and 3rd fastest horses overall.

By following this method, you can determine the top 3 horses with a total of 8 races (5 initial group races + 1 overall ranking race + 2 additional races for ranking).
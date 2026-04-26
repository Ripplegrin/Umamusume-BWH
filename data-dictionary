|Statistic| |Explanation| Equation|
| -------- | -------- |-------- |
|Shortstack Score |	If a given uma is shorter and bustier than the cast median, combines the distance from those medians.	|if(and(heightDiff<0,bustDiff>0),1,-1) * (abs(heightDiff)+abs(bustDiff))|
|Tallboard Score |	If a given uma is taller and flatter than the cast median, combines the distance from those medians.	|if(and(heightDiff>0,bustDiff<0),1,-1) * (abs(heightDiff)+abs(bustDiff))|
|TBHS (Top/Bottom-Heaviness Scale)|	Compares raw bust and hip measurements proportionally. 0 is balanced, positive number indicates top-heaviness, negative indicates bottom-heaviness. The farther from 0, the greater the degree.|	((bust/hips)-1)*100|
|Hourglass Quotient|	Averages bust and hip measurements and compares with waist. A higher number indicates a curvier overall shape, with a completely vertical torso scoring a 0.	(((bust+hips)/2)/waist)-1|
|aDR (adjusted Donk Rating)|	Expresses the difference between waist and hip circumference, with slight additional weighting of raw hip measurement.|	(hips-waist)*(hips/20)|
|Oatmeal%|	Measures lower-body thickness by comparing combined waist and hip measurements to height.	|((waist+hips)/height)3|
|T-Index (Todo Index)|	Examines applicability of the desciptors “tall” and “with a big ass”. A higher value indicates a greater degree of applicability of both, with a negative score indicating that one or both do not apply.	|(((height-medianHeight)*2)+aDR)-100|

# pi day
![alt tag](https://github.com/drJAGartner/pi_day/blob/master/happyPiDay.png)

To estimate pi, we can compare the ratio of the area of a circle to a square (or in our case, a quarter circle to a square.  Examine the following image:

![alt tag](https://github.com/drJAGartner/pi_day/blob/master/numberLine.png)

Here, you can see we have a circle which is centered at coordinate (0,0), with a radius of 1.  
If we consider throwing darts (generating random numbers) in the area between (0,0), and (1,1), 
the number of hits inside the circle, when compared to the the total number thrown, will be proportional
to the area of the circle over the area of the square.  Mathmatically this is
### a_circle = pi*r^2/4 = pi/4
### a_square = r^2 = 1
### a_circle/a_square = pi/4
### => pi = 4*(a_circle/a_square) = 4*(number of points in circle/total number of points)

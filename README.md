# SigmaGeek-Tetrahedron-Challenge
In this repository there is a code I made to calculate how many tetrahedrons are in the vertices and in the midpoints of the faces of an octahedron, as seen in [this challenge](https://sigmageek.com/polyhedral_results/polyhedral-computational-challenge).

To anyone curious about the answer, there are 10.

To run the code all you need to do is run `python3 findTetrahedrons.py` in your closest terminal.

While the code won't tell you the answer straight away like I did, it'll show all the points where the tetrahedrons could be.

In the code the edges of the octahedron have size √2, to make things easier.
The midpoints are located at  ±1/3, ±1/3, ±1/3 as they are the only points where you could feasibly fit a tetrahedron inside the octahedron.

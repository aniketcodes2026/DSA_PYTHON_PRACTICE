# Problem: Polar Coordinates
# Platform: HackerRank
# Concept: Math / Complex Numbers

import cmath

z = complex(input())

print(abs(z)) #prints the magnitude of the complex number z, which represents the polar coordinates of the complex number in the form (r, θ) where r is the magnitude and θ is the phase angle in radians.
print(cmath.phase(z)) #prints the magnitude and phase of the complex number z, which represents the polar coordinates of the complex number in the form (r, θ) where r is the magnitude and θ is the phase angle in radians.
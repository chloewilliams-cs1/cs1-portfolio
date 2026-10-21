#PiApproximation.py


"""We are going to approximate pi to any desired degree of accurancy by the infinite series
4- 4 / 3 + 4 / 5 - 4/7 + ..."""


print("We are finding the minimum number of terms needed to get an approximation of pi accurate within our error tolerance.")

error = float(input("Input error tolerance:"))

terms = 1
pi_approx = 0
pi = 3.14159265358979 

print("Numbers of Terms \t Pi Approximation")

while abs(pi - pi_approx) > error:
    pi_end = 4 * (-1) ** (terms + 1) / (2* terms -1)
    pi_approx += pi_end
    print(f"{terms} \t                \t {pi_approx:.6f}")
    terms += 1


print(f"After {terms} terms, pi is approximately {pi_approx:.6f}.")
print(f"Our error is {abs(pi - pi_approx):.6f} which is less than or equal to {error:.6f}.")
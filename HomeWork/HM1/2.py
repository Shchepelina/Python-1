#2. Напишите программу для проверки ложности утверждения
#(W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

for W in range(2):
        for Z in range(2):
            for V in range(2):
                print(not (W or Z or V) == (not W and not Z and not V))
                print(W, V, Z)


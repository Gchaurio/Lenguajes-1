-- 5.b)
data Arbol a = Hoja | Rama a (Arbol a) (Arbol a)

-- RESPUESTA --

foldA :: (a -> b -> b -> b) -> b -> Arbol a -> b
foldA _ i Hoja = i 
foldA f i (Rama value left right) = f value (foldA f i left) (foldA f i right)
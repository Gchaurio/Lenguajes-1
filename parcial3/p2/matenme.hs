import Control.Concurrent
import Control.Concurrent.MVar
import Control.Monad

-- Calcula el producto punto de dos segmentos de vectores
dotProductSegment :: [Int] -> [Int] -> IO Int
dotProductSegment xs ys = return $ sum $ zipWith (*) xs ys

-- Divide los vectores y procesa cada segmento concurrentemente
dotProductConcurrent :: [Int] -> [Int] -> IO Int
dotProductConcurrent xs ys = do
    let pairs = zip xs ys
        n = length pairs `div` 2
        (segment1, segment2) = splitAt n pairs
        processSegment = uncurry dotProductSegment . unzip

    result1 <- newEmptyMVar
    result2 <- newEmptyMVar

    forkIO $ processSegment segment1 >>= putMVar result1
    forkIO $ processSegment segment2 >>= putMVar result2

    r1 <- takeMVar result1
    r2 <- takeMVar result2
    return (r1 + r2)

-- Funcion de test
main :: IO ()
main = do
    let vec1 = [1, 2, 3]
        vec2 = [4, 5, 6]
    result <- dotProductConcurrent vec1 vec2
    print result
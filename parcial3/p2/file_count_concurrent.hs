import System.Directory
import System.FilePath ((</>))
import Control.Concurrent
import Control.Monad
import Data.List (isSuffixOf)
import Data.Maybe (catMaybes)

-- Funcion para contar archivos en un directorio y sus subdirectorios
countFiles :: FilePath -> IO Int
countFiles path = do
    contents <- listDirectory path
    paths <- forM contents $ \name -> do
        let fullPath = path </> name
        isDir <- doesDirectoryExist fullPath
        if isDir
            then do
                countVar <- newEmptyMVar
                forkIO $ countFiles fullPath >>= putMVar countVar
                return $ Just countVar
            else return Nothing

    let mvars = catMaybes paths
    counts <- mapM takeMVar mvars
    return $ length (filter (not . isSuffixOf "/") contents) + sum counts

-- Función principal
main :: IO ()
main = do
    putStrLn "Ingrese el path del directorio:"
    path <- getLine
    totalFiles <- countFiles path
    putStrLn $ "Total de archivos: " ++ show totalFiles
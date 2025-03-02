module spec GHC.Base where

import GHC.CString
import GHC.Classes
import GHC.Types
import GHC.Tuple

GHC.Base.. :: forall <p :: b -> c -> Bool, q :: a -> b -> Bool, r :: a -> c -> Bool>. 
                   {xcmp::a, wcmp::b<q xcmp> |- c<p wcmp> <: c<r xcmp>}
                   (ycmp:b -> c<p ycmp>)
                -> (zcmp:a -> b<q zcmp>)
                ->  xcmp:a -> c<r xcmp>

qualif Fst(__v:a, __y:b): (__v = (fst __y))
qualif Snd(__v:a, __y:b): (__v = (snd __y))

invariant {v: [a] | len v >= 0 }
map       :: (a -> b) -> xs:[a] -> {v: [b] | len v == len xs}
(++)      :: xs:[a] -> ys:[a] -> {v:[a] | len v == len xs + len ys}

($)       :: (a -> b) -> a -> b
id        :: x:a -> {v:a | v = x}

fmap      :: (a -> b) -> f a -> f b

qualif IsEmp(v:GHC.Types.Bool, xs: [a]) : (v <=> (len xs > 0))
qualif IsEmp(v:GHC.Types.Bool, xs: [a]) : (v <=> (len xs = 0))

qualif ListZ(v: [a])          : (len v =  0) 
qualif ListZ(v: [a])          : (len v >= 0) 
qualif ListZ(v: [a])          : (len v >  0) 

qualif CmpLen(v:[a], xs:[b])  : (len v  =  len xs ) 
qualif CmpLen(v:[a], xs:[b])  : (len v  >= len xs ) 
qualif CmpLen(v:[a], xs:[b])  : (len v  >  len xs ) 
qualif CmpLen(v:[a], xs:[b])  : (len v  <= len xs ) 
qualif CmpLen(v:[a], xs:[b])  : (len v  <  len xs ) 

qualif EqLen(v:int, xs: [a])  : (v = len xs ) 
qualif LenEq(v:[a], x: int)   : (x = len v ) 

qualif LenDiff(v:[a], x:int)  : (len v  = x + 1)
qualif LenDiff(v:[a], x:int)  : (len v  = x - 1)
qualif LenAcc(v:int, xs:[a], n: int): (v = len xs  + n)

{-# LANGUAGE Trustworthy #-}
{-@ LIQUID "--exact-data-con" @-}
module Data.Semigroup (module Exports) where

import GHC.List
import GHC.Num
import GHC.Types

import "base" Data.Semigroup as Exports

{-@ len :: forall a. [a] -> GHC.Types.Int @-}
{-@ reflect len @-}
len :: [a] -> Int
len [] = 0
len (_:l) = 1 + len l

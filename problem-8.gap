#Solutions to problem 8

# (a)
S           := JonesMonoid(7);;
J_7         := JonesMonoid(7);;
Ideals_J_7  := Ideals(J_7);;
List(Ideals_J_7, Size); # returns [429, 428, 392, 196]
Splash(DotString(J_7)); # displays that ideals are chain (induced by rank)
List(Ideals_J_7, I -> RankOfBipartition(Representative(I))); # returns [ 7, 5, 3, 1 ]

List(Ideals_J_7, I -> Size(TranslationalHull(I))); # returns [429, 429, 429, 123476695691247935826229781856256]

# (b)

List(Ideals_J_7, I -> Size(InnerTranslationalHull(I)) = Size(I));
# returns [true, true, true, true] - all ideals are weakly reductive

# (c)

# From (a), we know that the first three ideals are probably densely embedded as their translational hulls
# have the same size as J_7, but the last one is not.
# We need to check that e.g. the homomorphism from J_7 to Omega(I) is injective.

InducedBitranslation := function(I, x)
  local L, R, H, l, r;;
  L := LeftTranslations(I);;
  R := RightTranslations(I);;
  H := TranslationalHull(I);;
  l := LeftTranslation(L, MappingByFunction(I, I, i -> x * i));;
  r := RightTranslation(R, MappingByFunction(I, I, i -> i * x));;
  return Bitranslation(H, l, r);
# It would be more efficient to use e.g. LeftTranslationNC to avoid checking that the map is
# valid, but this is (currently) undocumented.
end;

for I in Ideals_J_7 do
  Rank_I := RankOfBipartition(Representative(I));;
  Image_Hom := Set(J_7, x -> InducedBitranslation(I, x));;
  if Size(Image_Hom) = Size(J_7) then
    Print("homomorphism J_7 -> Omega(I) is injective for rank ", Rank_I, "\n");
  fi;
od;

# so the first three ideals are densely embedded, but the last one is not

# (d)

# Checking the known properties of the smallest ideal, we find

KnownTruePropertiesOfObject(Ideals_J_7[4]);
# [ "IsNonTrivial", "IsFinite", "IsDuplicateFree", "IsAssociative", "IsFinitelyGeneratedMagma", "IsGeneratorsOfSemigroup", "IsSimpleSemigroup", "IsRegularSemigroup",
#  "IsBand", "IsCompletelyRegularSemigroup", "IsCompletelySimpleSemigroup", "IsIdempotentGenerated", "IsRectangularBand", "IsSemiband", "IsSemigroupIdeal",
#  "IsStarSemigroup", "CanUseLibsemigroupsFroidurePin", "CanUseGapFroidurePin", "CanUseFroidurePin", "IsActingSemigroupWithFixedDegreeMultiplication", "IsHTrivial",
#  "IsSurjectiveSemigroup", "CanUseLibsemigroupsCongruences" ]

# Compare this to one of the others:

KnownTruePropertiesOfObject(Ideals_J_7[1]);
# [ "IsNonTrivial", "IsFinite", "IsDuplicateFree", "IsAssociative", "IsFinitelyGeneratedMagma", "IsGeneratorsOfSemigroup", "IsRegularSemigroup", "IsSemigroupIdeal",
#  "IsStarSemigroup", "CanUseLibsemigroupsFroidurePin", "CanUseGapFroidurePin", "CanUseFroidurePin", "IsActingSemigroupWithFixedDegreeMultiplication",
#  "IsSurjectiveSemigroup", "CanUseLibsemigroupsCongruences" ]

# There are many a number of properties that are known to be true for the smallest ideal but not the others. In this case the most
# specific one, and the one that is actually being used, is IsRectangularBand:

I := Ideals_J_7[4];;
R := RectangularBand(NrRClasses(I), NrLClasses(I));;
Size(TranslationalHull(I)); #returns 123476695691247935826229781856256
MaybeSn := function(n)
  local F, R, i, j, k;
	
	F := FreeMonoid(n - 1);
	R := [];

	for i in [2 .. n] do
		Add(R, [F.(i - 1) ^ 2, One(F)]);
		for j in [2 .. n] do
			if i <> j then
				Add(R, [(F.(i - 1) * F.(j - 1)) ^ 3, One(F)]);
        for k in [2 .. n] do
          if k <> j and k <> i then
            Add(R, [(F.(i - 1) * F.(j - 1) * F.(k - 1)) ^ 4, One(F)]);
          fi;
        od;
			fi;
		od;
  od;
	return F / R;
end;

Size(MaybeSn(1)); # returns 1 (okay)
Size(MaybeSn(2)); # returns 2 (okay)
Size(MaybeSn(3)); # returns 6 (okay)
G := Range(IsomorphismPermGroup(MaybeSn(3)));
StructureDescription(G); # S3
Size(MaybeSn(4)); # returns 72 (not okay)
# Size(MaybeSn(5)) # seemingly runs forever
NumberOfRightCongruences(SymmetricGroup(5), 3); # returns 2
NumberOfRightCongruences(MaybeSn(5), 3);        # returns 41

NumberOfRightCongruences(SymmetricGroup(6), 3); # returns 2
NumberOfRightCongruences(MaybeSn(6), 3);        # returns 122

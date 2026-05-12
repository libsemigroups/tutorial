F := FreeSemigroup("a", "b", "c", "d", "e", "f", "g");
AssignGeneratorVariables(F);
R := ParseRelations(GeneratorsOfSemigroup(F), "abcd=aaaeaa,ef=dg");
S := F / R;

# Part (a)
Size(S); # returns infinity

# Part (b)
hom := SemigroupHomomorphismByImages(F, S, Generators(F), Generators(S));

# Part (c)
PartitionByFunc2 := 
function ( list, func )
    local blist, nr, out, val, i, j;
    blist := BlistList( [ 1 .. Length( list ) ], [  ] );
    nr := 0;
    out := [  ];
    for i in [ 1 .. Length( list ) ] do
        if not blist[i] then
            nr := nr + 1;
            blist[i] := true;
            out[nr] := [ list[i] ];
            val := func( list[i] );
            for j in [ i + 1 .. Length( list ) ] do
                if not blist[j] and func( list[j] ) = val then
                    blist[j] := true;
                    Add( out[nr], list[j] );
                fi;
            od;
        fi;
    od;
    return out;
end;

PartitionByFunc2(enum{[1 .. 1000]}, hom);

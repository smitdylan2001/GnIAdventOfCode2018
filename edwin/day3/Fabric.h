#pragma once


#include "Claim.h"
#include <set>

#define ROWS 1000
#define COLUMNS 1000

class Fabric {
    private:
        int squares[COLUMNS * ROWS];
        std::set<int> nonOverlappingClaims;

    public:
        Fabric();
        void wipe();
        void applyClaim(const Claim& claim);
        long countContestedSquares();
        void applyOverlap(const Claim& claim);
        int findNonOverlappingClaim();
};


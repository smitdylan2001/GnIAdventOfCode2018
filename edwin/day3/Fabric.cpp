#include <set>
#include <iostream>
#include "Fabric.h"

Fabric::Fabric() {}

void Fabric::applyClaim(const Claim& claim) {
    for (int i = 0; i < claim.width; ++i) {
        for (int j = 0; j < claim.height; ++j) {
            squares[claim.x + claim.y * COLUMNS + i + j * COLUMNS]++;
        }
    }
}

void Fabric::wipe() {
    memset(squares, 0, sizeof(squares));
}

long Fabric::countContestedSquares() {
    return std::count_if(std::begin(squares), std::end(squares), [&](int square) { return square > 1; });
}

void Fabric::applyOverlap(const Claim& claim) {
    bool hasOverlap = false;
    for (int i = 0; i < claim.width; ++i) {
        for (int j = 0; j < claim.height; ++j) {
            if (squares[claim.x + claim.y * COLUMNS + i + j * COLUMNS] == 0) {
                squares[claim.x + claim.y * COLUMNS + i + j * COLUMNS] = claim.id;
            } else {
                hasOverlap = true;
                int currentClaim = squares[claim.x + claim.y * COLUMNS + i + j * COLUMNS];
                nonOverlappingClaims.erase(currentClaim);
            }
        }
    }
    if (!hasOverlap) nonOverlappingClaims.insert(claim.id);
}

int Fabric::findNonOverlappingClaim() {
    if (nonOverlappingClaims.size() != 1) std::cout << "uhoh" << std::endl;
    return *nonOverlappingClaims.begin();
}


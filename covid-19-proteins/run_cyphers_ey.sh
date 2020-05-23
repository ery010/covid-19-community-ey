#!/bin/bash

DEFAULT_ENDPOINT=bolt://localhost:11006
ENDPOINT=${NEO4J_URI:-$DEFAULT_ENDPOINT}
USERNAME=${NEO4J_USERNAME:-neo4j}
PASSWORD=${NEO4J_PASSWORD:-neo4jbinder}
CYPHERS="../cyphers"
REFDATA="../reference_data"

echo "Endpoint: "$ENDPOINT
echo "Username: "$USERNAME
echo "Password: "$PASSWORD

export cypher_shell="$NEO4J_HOME/bin/cypher-shell"

function run_cypher {
    echo " "
    echo "----------------------------------------------"
    echo "Running $1:"
    echo " "
    cat "$CYPHERS/$1"
    cat "$CYPHERS/$1" | "$cypher_shell" -a "$ENDPOINT" -u "$USERNAME" -p "$PASSWORD"
}

# Copy reference files to the Neo4j import directory
cp $REFDATA/Organism.csv "$NEO4J_HOME"/import
cp $REFDATA/Outbreak.csv "$NEO4J_HOME"/import
cp $REFDATA/Continent.csv "$NEO4J_HOME"/import
cp $REFDATA/interactions.csv "$NEO4J_HOME"/import
cp $REFDATA/human_data.csv "$NEO4J_HOME"/import
cp $REFDATA/human_alias.csv "$NEO4J_HOME"/import
cp $REFDATA/virus_data.csv "$NEO4J_HOME"/import
cp $REFDATA/virus_alias.csv "$NEO4J_HOME"/import


# Set up the database
run_cypher 00a-Init.cypher
run_cypher 00b-Organism.cypher
run_cypher 00c-Outbreak.cypher
run_cypher 00d-Continent.cypher
run_cypher 00e-GeoNamesCountry.cypher
run_cypher 00f-GeoNamesAdmin1.cypher
run_cypher 00g-GeoNamesAdmin2.cypher
run_cypher 00h-GeoNamesCity.cypher
run_cypher 00i-USCensusRegionDivisionState2017.cypher
run_cypher 00j-USCensusCountyCity2017.cypher
run_cypher 01a-NCBIStrain.cypher
run_cypher 01b-Nextstrain.cypher
run_cypher 01c-NCBIRefSeq.cypher
run_cypher 01d-PMC-Accession.cypher
run_cypher protein_interactions.cypher
run_cypher interactions.cypher

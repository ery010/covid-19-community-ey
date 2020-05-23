LOAD CSV WITH HEADERS 
FROM 'FILE:///interactions.csv' AS row 
MERGE (i:interactions{Interaction_ID: row.Interaction_ID})
SET i.SARS_COV2_Protein_ID = row.SARS_COV2_Protein_ID, i.Human_Protein_ID = row.Human_Protein_ID
RETURN count(i) as interactions;
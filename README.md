# djangoproject00

In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.

Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.

These concepts are represented by Python classes. 

In our troubleshoot app, we'll create four models : EcoFlush_Models, Issues, troubleshoot techniques, and diagnosis. A EcoFlush_Model has 4 models attributes (B8100,B8104,B8106,B8106s) . An Issue has 4 fields : LEAKING , CONSTANTLY RUNNING, NOT FLUSHING,&  WEAK FLUSH. Trouble shooting techniques has 3 fields: CLEAN_FILTER, MANUEL_FLUSH, and CHECK_USA  .

Each issue is associated with a model, and each technique is associated with each issue.

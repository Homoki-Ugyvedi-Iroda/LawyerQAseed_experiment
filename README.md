# LawyerQAseed_experiment

This repository includes the files used for a simple lawyer-focused QA  used in relation to basic questions related to the Hungarian Civil Code and Code of Civil Procedure. Explanations are provided in a blogpost on the public website of Homoki Ügyvedédi Iroda (https://homoki.net).

The results of the evaluation are contained in an Excel workbook with multiple worksheets. The worksheet with GPT-3 was using also commentaries on the Civil Code and Procedure, but used slightly different questions (`GPT-3_emb_PtkPp_w_commentary`). Two worksheets contain the results of QA tasks using text embeddings for answers (`GPT-3.5_emb_PtkPp_no_commentary`, `GPT-4_emb_PtkPp_no_commentary`), where the GPT-4 model (being more expensive) was only used with the most promising approach (OpenAI embeddings and similarity search), while for GPT-3.5 (being cheaper), different retrieval and text embedding options were also compared (with not much of a difference in this very limited evaluation). Used https://autoevaluator.langchain.com/ for evaluating different retrieval techniques and text embedding options.

For comparison, the same questions were also asked from ChatGPT+ (both GPT-3.5 model and GPT-4 model, `GPT-4_ChatGPT_no_embed`, `GPT-3.5_ChatGPT_no_embedd`) where no text embeddings were used, just the pre-trained knowledge of the LLM. The results were clearly better when based on text embeddings.

In the "human evaluation" column, 0 means a clearly incorrect answer, 1 means an acceptable (largely correct) answer.

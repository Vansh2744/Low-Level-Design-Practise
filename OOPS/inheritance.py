class RAG():
    def __init__(self, file:str):
        self.file = file

    def embeddings(self, text:str):
        return text

    def vector_store(self):
        print(f"Stored Embeddings of File: {self.file}")

class PDFUpload(RAG):
    def upload_pdf(self):
        return "Hello My Name is Vansh"

class YTUpload(RAG):
    def __init__(self, file:str, duration:str):
        super().__init__(file)
        self.duration = duration

    def upload_yt(self):
        return "Python Playlist"

pdf = PDFUpload('my_notes.pdf')
pdf_txt = pdf.upload_pdf()
emb = pdf.embeddings(pdf_txt)
pdf.vector_store()

yt = YTUpload('python.mp4', '23 min')
yt_txt = yt.upload_yt()
yt_emb = yt.embeddings(yt_txt)
yt.vector_store()
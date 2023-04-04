from ansi.colour import fg, bg
from source.listening import listen_petition as lsp
from source.generate_text_gpt3 import generate_text as gt
from source.generate_audio import generate_audio as ga

if __name__=='__main__':
    resp_lsp = lsp()
    print(fg.red(f"Listing: {resp_lsp}"))
    resp_gt = gt(resp_lsp)
    print(fg.blue(f"Result gpt3 \n{resp_gt}"))
    ga(resp_gt)
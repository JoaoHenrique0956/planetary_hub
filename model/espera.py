import os

class Espera:
    def __init__(self):
 
        self.caminho_padrao = r"C:\Users\sa_salainterativa\Desktop\planetary_hub\videos\videos_espera"

    def reproduzir_video(self, caminho_video):
        """
        Recebe o caminho de um vídeo e abre
        usando o reprodutor padrão do Windows.
        """
   
        if not os.path.isfile(caminho_video):
            print("Vídeo não encontrado:", caminho_video)
            return False

        # Abre o vídeo no programa padrão do Windows
        os.startfile(caminho_video)
        return True

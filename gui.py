from PySimpleGUI import PySimpleGUI as sg

nomeM = ''

def janela_cadastro_pai():
    sg.theme('Dark Amber')
    layout = [
        [sg.Text('NOME DO PAI'), sg.Input(key='-PAI-')],

        [sg.Text('CABELO'), sg.Radio('castanho', 'hair_id', key='cabelo', default=False),
        sg.Radio('loiro', 'hair_id', key='cabelo', default=False)],

        [sg.Text('ETINIA'), sg.Radio('branco', 'person_id', key='etinia', default=False), 
        sg.Radio('preto', 'person_id', key='etinia', default=False)],

        [sg.Text('OLHO'), sg.Radio('verde', 'eye_id', key='olho', default=False), 
        sg.Radio('castanho', 'eye_id', key='olho', default=False), 
        sg.Radio('azul', 'eye_id', key='olho', default=False)],

        [sg.Button('ENVIAR')]
    ]
    return sg.Window('Cadastro Pai', layout=layout, finalize=True)


def janela_cadastro_mae():
    sg.theme('Dark Amber')
    layout = [
        [sg.Text('NOME DA MÃE'), sg.Input(key='-MAE-')],
            
        [sg.Text('CABELO'), sg.Radio('castanho', 'hair_id', key='cabelo', default=False),
        sg.Radio('loiro', 'hair_id', key='cabelo', default=False)],

        [sg.Text('ETINIA'), sg.Radio('branco', 'person_id', key='etinia', default=False), 
        sg.Radio('preto', 'person_id', key='etinia', default=False)],

        [sg.Text('OLHO'), sg.Radio('verde', 'eye_id', key='olho', default=False), 
        sg.Radio('castanho', 'eye_id', key='olho', default=False), 
        sg.Radio('azul', 'eye_id', key='olho', default=False)],

        [sg.Button('VOLTAR'), sg.Button('ENVIAR')]
        
    ]
    return sg.Window('Cadastro Mãe', layout=layout, finalize=True)


# criar janela
janela1, janela2 = janela_cadastro_pai(),None

def format_input_information(values):
    information = "Cadastros feitos!"
    name = '\nPai: ' + values['-PAI-']
    name2 = '\nMãe: ' + values['-MAE-']
    information += name
    information += name2
    
    return information



#eventos
while True:
    windown,event,values = sg.read_all_windows()
    #exite
    if windown == janela1 and event == sg.WIN_CLOSED:
        break
    #next

    if windown == janela1 and event == 'ENVIAR':
        janela2 = janela_cadastro_mae()
        janela1.hide()
    if windown == janela2 and event == 'VOLTAR':
        janela2.hide()
        janela1.un_hide()
    if windown == janela2 and event == 'ENVIAR':
        sg.popup(format_input_information(values))
         
        


windown.Close()
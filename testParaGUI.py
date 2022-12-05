from PySimpleGUI import PySimpleGUI as sg




sg.theme('Dark Amber')
layoutPai = [
    [sg.Text('NOME DO PAI'), sg.Input(key='-PAI-')],

    [sg.Text('CABELO'), sg.Radio('castanho', 'hair_id', key='cabelo', default=False),
    sg.Radio('loiro', 'hair_id', key='cabelo', default=False)],

    [sg.Text('ETINIA'), sg.Radio('branco', 'person_id', key='etinia', default=False), 
    sg.Radio('preto', 'person_id', key='etinia', default=False)],

    [sg.Text('OLHO'), sg.Radio('verde', 'eye_id', key='olho', default=False), 
    sg.Radio('castanho', 'eye_id', key='olho', default=False), 
    sg.Radio('azul', 'eye_id', key='olho', default=False)],

    [sg.Button('ENVIAR'), sg.Exit()]
]

sg.theme('Dark Amber')
layoutMae = [
    [sg.Text('NOME DA MÃE'), sg.Input(key='-MAE-')],

    [sg.Text('CABELO'), sg.Radio('castanho', 'hair_id', key='cabelo', default=False),
    sg.Radio('loiro', 'hair_id', key='cabelo', default=False)],

    [sg.Text('ETINIA'), sg.Radio('branco', 'person_id', key='etinia', default=False), 
    sg.Radio('preto', 'person_id', key='etinia', default=False)],

    [sg.Text('OLHO'), sg.Radio('verde', 'eye_id', key='olho', default=False), 
    sg.Radio('castanho', 'eye_id', key='olho', default=False), 
    sg.Radio('azul', 'eye_id', key='olho', default=False)],

    [sg.Button('ENVIAR'), sg.Exit()]
]

janela1= layoutPai
janela2 = layoutMae

# criar janela
windown = sg.Window('Teste', layout=janela1)






def format_input_information(values):
    information = "Cadastros feitos!"
    name = '\nPai: ' + values['-PAI-']
    information += name
    
    return information



#eventos
while True:
    event,values = windown.read()
    #exite
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    #next

    if windown == janela1 and event == 'ENVIAR':
        janela1 = layoutMae
        janela1.hide()

    if event == 'ENVIAR':
        sg.popup(format_input_information(values))

         
        
        

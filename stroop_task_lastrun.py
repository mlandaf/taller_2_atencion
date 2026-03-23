#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.2),
    on Marzo 23, 2026, at 10:53
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.2'
expName = 'stroop_task'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1024,768]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\evento\\Desktop\\investigacion_neuro\\Semana 7 - Atencion\\taller_2_atencion\\stroop_task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = (-1.0000, -1.0000, -1.0000)
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instrucciones" ---
    instrucciones_image = visual.ImageStim(
        win=win,
        name='instrucciones_image', 
        image='media/instructions/1_instrucciones.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "inicio_practica" ---
    inicio_practica_image = visual.ImageStim(
        win=win,
        name='inicio_practica_image', 
        image='media/instructions/2_inicio_practica.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_2 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "practica" ---
    fix_cross_practice = visual.ShapeStim(
        win=win, name='fix_cross_practice', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    palabra_practica_txt = visual.TextStim(win=win, name='palabra_practica_txt',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_practice = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "feedback_practica" ---
    feedback_text = visual.TextStim(win=win, name='feedback_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "fin_practica" ---
    fin_practica_image = visual.ImageStim(
        win=win,
        name='fin_practica_image', 
        image='media/instructions/3_fin_practica.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "descanso" ---
    descanso_image = visual.ImageStim(
        win=win,
        name='descanso_image', 
        image='media/instructions/4_descanso.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "inicio_experimental" ---
    inicio_experimental_image = visual.ImageStim(
        win=win,
        name='inicio_experimental_image', 
        image='media/instructions/5_inicio_experimental.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_3 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "experimental" ---
    fix_cross_experimental = visual.ShapeStim(
        win=win, name='fix_cross_experimental', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    palabra_experimental_text = visual.TextStim(win=win, name='palabra_experimental_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_4 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "ITI" ---
    ITI_text = visual.TextStim(win=win, name='ITI_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "fin_experimento" ---
    fin_experimento_image = visual.ImageStim(
        win=win,
        name='fin_experimento_image', 
        image='media/instructions/6_fin_experimento.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "instrucciones" ---
    # create an object to store info about Routine instrucciones
    instrucciones = data.Routine(
        name='instrucciones',
        components=[instrucciones_image, key_resp],
    )
    instrucciones.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for instrucciones
    instrucciones.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instrucciones.tStart = globalClock.getTime(format='float')
    instrucciones.status = STARTED
    thisExp.addData('instrucciones.started', instrucciones.tStart)
    instrucciones.maxDuration = None
    # keep track of which components have finished
    instruccionesComponents = instrucciones.components
    for thisComponent in instrucciones.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instrucciones" ---
    thisExp.currentRoutine = instrucciones
    instrucciones.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrucciones_image* updates
        
        # if instrucciones_image is starting this frame...
        if instrucciones_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrucciones_image.frameNStart = frameN  # exact frame index
            instrucciones_image.tStart = t  # local t and not account for scr refresh
            instrucciones_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrucciones_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrucciones_image.started')
            # update status
            instrucciones_image.status = STARTED
            instrucciones_image.setAutoDraw(True)
        
        # if instrucciones_image is active this frame...
        if instrucciones_image.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instrucciones,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instrucciones.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instrucciones.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instrucciones.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instrucciones" ---
    for thisComponent in instrucciones.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instrucciones
    instrucciones.tStop = globalClock.getTime(format='float')
    instrucciones.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instrucciones.stopped', instrucciones.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "instrucciones" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "inicio_practica" ---
    # create an object to store info about Routine inicio_practica
    inicio_practica = data.Routine(
        name='inicio_practica',
        components=[inicio_practica_image, key_resp_2],
    )
    inicio_practica.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for inicio_practica
    inicio_practica.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    inicio_practica.tStart = globalClock.getTime(format='float')
    inicio_practica.status = STARTED
    thisExp.addData('inicio_practica.started', inicio_practica.tStart)
    inicio_practica.maxDuration = None
    # keep track of which components have finished
    inicio_practicaComponents = inicio_practica.components
    for thisComponent in inicio_practica.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "inicio_practica" ---
    thisExp.currentRoutine = inicio_practica
    inicio_practica.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inicio_practica_image* updates
        
        # if inicio_practica_image is starting this frame...
        if inicio_practica_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inicio_practica_image.frameNStart = frameN  # exact frame index
            inicio_practica_image.tStart = t  # local t and not account for scr refresh
            inicio_practica_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inicio_practica_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'inicio_practica_image.started')
            # update status
            inicio_practica_image.status = STARTED
            inicio_practica_image.setAutoDraw(True)
        
        # if inicio_practica_image is active this frame...
        if inicio_practica_image.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=inicio_practica,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            inicio_practica.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if inicio_practica.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in inicio_practica.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "inicio_practica" ---
    for thisComponent in inicio_practica.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for inicio_practica
    inicio_practica.tStop = globalClock.getTime(format='float')
    inicio_practica.tStopRefresh = tThisFlipGlobal
    thisExp.addData('inicio_practica.stopped', inicio_practica.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "inicio_practica" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_practica_stroop = data.TrialHandler2(
        name='loop_practica_stroop',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions/condiciones_practica_stroop.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(loop_practica_stroop)  # add the loop to the experiment
    thisLoop_practica_stroop = loop_practica_stroop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_practica_stroop.rgb)
    if thisLoop_practica_stroop != None:
        for paramName in thisLoop_practica_stroop:
            globals()[paramName] = thisLoop_practica_stroop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_practica_stroop in loop_practica_stroop:
        loop_practica_stroop.status = STARTED
        if hasattr(thisLoop_practica_stroop, 'status'):
            thisLoop_practica_stroop.status = STARTED
        currentLoop = loop_practica_stroop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_practica_stroop.rgb)
        if thisLoop_practica_stroop != None:
            for paramName in thisLoop_practica_stroop:
                globals()[paramName] = thisLoop_practica_stroop[paramName]
        
        # --- Prepare to start Routine "practica" ---
        # create an object to store info about Routine practica
        practica = data.Routine(
            name='practica',
            components=[fix_cross_practice, palabra_practica_txt, key_resp_practice],
        )
        practica.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        palabra_practica_txt.setColor(color_tinta_p, colorSpace='rgb')
        palabra_practica_txt.setText(palabra_p)
        # create starting attributes for key_resp_practice
        key_resp_practice.keys = []
        key_resp_practice.rt = []
        _key_resp_practice_allKeys = []
        # store start times for practica
        practica.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practica.tStart = globalClock.getTime(format='float')
        practica.status = STARTED
        thisExp.addData('practica.started', practica.tStart)
        practica.maxDuration = None
        # keep track of which components have finished
        practicaComponents = practica.components
        for thisComponent in practica.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practica" ---
        thisExp.currentRoutine = practica
        practica.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_practica_stroop, 'status') and thisLoop_practica_stroop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_cross_practice* updates
            
            # if fix_cross_practice is starting this frame...
            if fix_cross_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross_practice.frameNStart = frameN  # exact frame index
                fix_cross_practice.tStart = t  # local t and not account for scr refresh
                fix_cross_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_cross_practice.started')
                # update status
                fix_cross_practice.status = STARTED
                fix_cross_practice.setAutoDraw(True)
            
            # if fix_cross_practice is active this frame...
            if fix_cross_practice.status == STARTED:
                # update params
                pass
            
            # if fix_cross_practice is stopping this frame...
            if fix_cross_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_cross_practice.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_cross_practice.tStop = t  # not accounting for scr refresh
                    fix_cross_practice.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_cross_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_cross_practice.stopped')
                    # update status
                    fix_cross_practice.status = FINISHED
                    fix_cross_practice.setAutoDraw(False)
            
            # *palabra_practica_txt* updates
            
            # if palabra_practica_txt is starting this frame...
            if palabra_practica_txt.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                palabra_practica_txt.frameNStart = frameN  # exact frame index
                palabra_practica_txt.tStart = t  # local t and not account for scr refresh
                palabra_practica_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(palabra_practica_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'palabra_practica_txt.started')
                # update status
                palabra_practica_txt.status = STARTED
                palabra_practica_txt.setAutoDraw(True)
            
            # if palabra_practica_txt is active this frame...
            if palabra_practica_txt.status == STARTED:
                # update params
                pass
            
            # if palabra_practica_txt is stopping this frame...
            if palabra_practica_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > palabra_practica_txt.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    palabra_practica_txt.tStop = t  # not accounting for scr refresh
                    palabra_practica_txt.tStopRefresh = tThisFlipGlobal  # on global time
                    palabra_practica_txt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'palabra_practica_txt.stopped')
                    # update status
                    palabra_practica_txt.status = FINISHED
                    palabra_practica_txt.setAutoDraw(False)
            
            # *key_resp_practice* updates
            waitOnFlip = False
            
            # if key_resp_practice is starting this frame...
            if key_resp_practice.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_practice.frameNStart = frameN  # exact frame index
                key_resp_practice.tStart = t  # local t and not account for scr refresh
                key_resp_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_practice.started')
                # update status
                key_resp_practice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_practice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_practice is stopping this frame...
            if key_resp_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_practice.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_practice.tStop = t  # not accounting for scr refresh
                    key_resp_practice.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_practice.stopped')
                    # update status
                    key_resp_practice.status = FINISHED
                    key_resp_practice.status = FINISHED
            if key_resp_practice.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_practice.getKeys(keyList=['a','s','k','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_practice_allKeys.extend(theseKeys)
                if len(_key_resp_practice_allKeys):
                    key_resp_practice.keys = _key_resp_practice_allKeys[-1].name  # just the last key pressed
                    key_resp_practice.rt = _key_resp_practice_allKeys[-1].rt
                    key_resp_practice.duration = _key_resp_practice_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_practice.keys == str(tecla_correcta_p)) or (key_resp_practice.keys == tecla_correcta_p):
                        key_resp_practice.corr = 1
                    else:
                        key_resp_practice.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=practica,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                practica.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if practica.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in practica.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practica" ---
        for thisComponent in practica.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practica
        practica.tStop = globalClock.getTime(format='float')
        practica.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practica.stopped', practica.tStop)
        # check responses
        if key_resp_practice.keys in ['', [], None]:  # No response was made
            key_resp_practice.keys = None
            # was no response the correct answer?!
            if str(tecla_correcta_p).lower() == 'none':
               key_resp_practice.corr = 1;  # correct non-response
            else:
               key_resp_practice.corr = 0;  # failed to respond (incorrectly)
        # store data for loop_practica_stroop (TrialHandler)
        loop_practica_stroop.addData('key_resp_practice.keys',key_resp_practice.keys)
        loop_practica_stroop.addData('key_resp_practice.corr', key_resp_practice.corr)
        if key_resp_practice.keys != None:  # we had a response
            loop_practica_stroop.addData('key_resp_practice.rt', key_resp_practice.rt)
            loop_practica_stroop.addData('key_resp_practice.duration', key_resp_practice.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if practica.maxDurationReached:
            routineTimer.addTime(-practica.maxDuration)
        elif practica.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "feedback_practica" ---
        # create an object to store info about Routine feedback_practica
        feedback_practica = data.Routine(
            name='feedback_practica',
            components=[feedback_text],
        )
        feedback_practica.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        mensaje_feedback = ""
        if key_resp_practice.corr == 1:
            mensaje_feedback = "¡Correcto!"
        else:
            mensaje_feedback = "Incorrecto"
        feedback_text.setText(mensaje_feedback)
        # store start times for feedback_practica
        feedback_practica.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback_practica.tStart = globalClock.getTime(format='float')
        feedback_practica.status = STARTED
        thisExp.addData('feedback_practica.started', feedback_practica.tStart)
        feedback_practica.maxDuration = None
        # keep track of which components have finished
        feedback_practicaComponents = feedback_practica.components
        for thisComponent in feedback_practica.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback_practica" ---
        thisExp.currentRoutine = feedback_practica
        feedback_practica.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.1:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_practica_stroop, 'status') and thisLoop_practica_stroop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            
            # if feedback_text is starting this frame...
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.started')
                # update status
                feedback_text.status = STARTED
                feedback_text.setAutoDraw(True)
            
            # if feedback_text is active this frame...
            if feedback_text.status == STARTED:
                # update params
                pass
            
            # if feedback_text is stopping this frame...
            if feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                    # update status
                    feedback_text.status = FINISHED
                    feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=feedback_practica,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                feedback_practica.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if feedback_practica.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in feedback_practica.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback_practica" ---
        for thisComponent in feedback_practica.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback_practica
        feedback_practica.tStop = globalClock.getTime(format='float')
        feedback_practica.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback_practica.stopped', feedback_practica.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback_practica.maxDurationReached:
            routineTimer.addTime(-feedback_practica.maxDuration)
        elif feedback_practica.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.100000)
        # mark thisLoop_practica_stroop as finished
        if hasattr(thisLoop_practica_stroop, 'status'):
            thisLoop_practica_stroop.status = FINISHED
        # if awaiting a pause, pause now
        if loop_practica_stroop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            loop_practica_stroop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'loop_practica_stroop'
    loop_practica_stroop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "fin_practica" ---
    # create an object to store info about Routine fin_practica
    fin_practica = data.Routine(
        name='fin_practica',
        components=[fin_practica_image],
    )
    fin_practica.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for fin_practica
    fin_practica.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    fin_practica.tStart = globalClock.getTime(format='float')
    fin_practica.status = STARTED
    thisExp.addData('fin_practica.started', fin_practica.tStart)
    fin_practica.maxDuration = None
    # keep track of which components have finished
    fin_practicaComponents = fin_practica.components
    for thisComponent in fin_practica.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fin_practica" ---
    thisExp.currentRoutine = fin_practica
    fin_practica.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fin_practica_image* updates
        
        # if fin_practica_image is starting this frame...
        if fin_practica_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fin_practica_image.frameNStart = frameN  # exact frame index
            fin_practica_image.tStart = t  # local t and not account for scr refresh
            fin_practica_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fin_practica_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fin_practica_image.started')
            # update status
            fin_practica_image.status = STARTED
            fin_practica_image.setAutoDraw(True)
        
        # if fin_practica_image is active this frame...
        if fin_practica_image.status == STARTED:
            # update params
            pass
        
        # if fin_practica_image is stopping this frame...
        if fin_practica_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fin_practica_image.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                fin_practica_image.tStop = t  # not accounting for scr refresh
                fin_practica_image.tStopRefresh = tThisFlipGlobal  # on global time
                fin_practica_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fin_practica_image.stopped')
                # update status
                fin_practica_image.status = FINISHED
                fin_practica_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=fin_practica,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            fin_practica.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if fin_practica.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in fin_practica.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fin_practica" ---
    for thisComponent in fin_practica.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for fin_practica
    fin_practica.tStop = globalClock.getTime(format='float')
    fin_practica.tStopRefresh = tThisFlipGlobal
    thisExp.addData('fin_practica.stopped', fin_practica.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if fin_practica.maxDurationReached:
        routineTimer.addTime(-fin_practica.maxDuration)
    elif fin_practica.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "descanso" ---
    # create an object to store info about Routine descanso
    descanso = data.Routine(
        name='descanso',
        components=[descanso_image],
    )
    descanso.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for descanso
    descanso.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    descanso.tStart = globalClock.getTime(format='float')
    descanso.status = STARTED
    thisExp.addData('descanso.started', descanso.tStart)
    descanso.maxDuration = None
    # keep track of which components have finished
    descansoComponents = descanso.components
    for thisComponent in descanso.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "descanso" ---
    thisExp.currentRoutine = descanso
    descanso.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 60.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *descanso_image* updates
        
        # if descanso_image is starting this frame...
        if descanso_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            descanso_image.frameNStart = frameN  # exact frame index
            descanso_image.tStart = t  # local t and not account for scr refresh
            descanso_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(descanso_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'descanso_image.started')
            # update status
            descanso_image.status = STARTED
            descanso_image.setAutoDraw(True)
        
        # if descanso_image is active this frame...
        if descanso_image.status == STARTED:
            # update params
            pass
        
        # if descanso_image is stopping this frame...
        if descanso_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > descanso_image.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                descanso_image.tStop = t  # not accounting for scr refresh
                descanso_image.tStopRefresh = tThisFlipGlobal  # on global time
                descanso_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'descanso_image.stopped')
                # update status
                descanso_image.status = FINISHED
                descanso_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=descanso,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            descanso.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if descanso.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in descanso.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "descanso" ---
    for thisComponent in descanso.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for descanso
    descanso.tStop = globalClock.getTime(format='float')
    descanso.tStopRefresh = tThisFlipGlobal
    thisExp.addData('descanso.stopped', descanso.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if descanso.maxDurationReached:
        routineTimer.addTime(-descanso.maxDuration)
    elif descanso.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-60.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "inicio_experimental" ---
    # create an object to store info about Routine inicio_experimental
    inicio_experimental = data.Routine(
        name='inicio_experimental',
        components=[inicio_experimental_image, key_resp_3],
    )
    inicio_experimental.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_3
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # store start times for inicio_experimental
    inicio_experimental.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    inicio_experimental.tStart = globalClock.getTime(format='float')
    inicio_experimental.status = STARTED
    thisExp.addData('inicio_experimental.started', inicio_experimental.tStart)
    inicio_experimental.maxDuration = None
    # keep track of which components have finished
    inicio_experimentalComponents = inicio_experimental.components
    for thisComponent in inicio_experimental.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "inicio_experimental" ---
    thisExp.currentRoutine = inicio_experimental
    inicio_experimental.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inicio_experimental_image* updates
        
        # if inicio_experimental_image is starting this frame...
        if inicio_experimental_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inicio_experimental_image.frameNStart = frameN  # exact frame index
            inicio_experimental_image.tStart = t  # local t and not account for scr refresh
            inicio_experimental_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inicio_experimental_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'inicio_experimental_image.started')
            # update status
            inicio_experimental_image.status = STARTED
            inicio_experimental_image.setAutoDraw(True)
        
        # if inicio_experimental_image is active this frame...
        if inicio_experimental_image.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=inicio_experimental,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            inicio_experimental.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if inicio_experimental.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in inicio_experimental.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "inicio_experimental" ---
    for thisComponent in inicio_experimental.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for inicio_experimental
    inicio_experimental.tStop = globalClock.getTime(format='float')
    inicio_experimental.tStopRefresh = tThisFlipGlobal
    thisExp.addData('inicio_experimental.stopped', inicio_experimental.tStop)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "inicio_experimental" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_experimental_stroop = data.TrialHandler2(
        name='loop_experimental_stroop',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions/condiciones_experimental_stroop.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(loop_experimental_stroop)  # add the loop to the experiment
    thisLoop_experimental_stroop = loop_experimental_stroop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_experimental_stroop.rgb)
    if thisLoop_experimental_stroop != None:
        for paramName in thisLoop_experimental_stroop:
            globals()[paramName] = thisLoop_experimental_stroop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_experimental_stroop in loop_experimental_stroop:
        loop_experimental_stroop.status = STARTED
        if hasattr(thisLoop_experimental_stroop, 'status'):
            thisLoop_experimental_stroop.status = STARTED
        currentLoop = loop_experimental_stroop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_experimental_stroop.rgb)
        if thisLoop_experimental_stroop != None:
            for paramName in thisLoop_experimental_stroop:
                globals()[paramName] = thisLoop_experimental_stroop[paramName]
        
        # --- Prepare to start Routine "experimental" ---
        # create an object to store info about Routine experimental
        experimental = data.Routine(
            name='experimental',
            components=[fix_cross_experimental, palabra_experimental_text, key_resp_4],
        )
        experimental.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        palabra_experimental_text.setColor(color_tinta, colorSpace='rgb')
        palabra_experimental_text.setText(palabra)
        # create starting attributes for key_resp_4
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # store start times for experimental
        experimental.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        experimental.tStart = globalClock.getTime(format='float')
        experimental.status = STARTED
        thisExp.addData('experimental.started', experimental.tStart)
        experimental.maxDuration = None
        # keep track of which components have finished
        experimentalComponents = experimental.components
        for thisComponent in experimental.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "experimental" ---
        thisExp.currentRoutine = experimental
        experimental.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_experimental_stroop, 'status') and thisLoop_experimental_stroop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_cross_experimental* updates
            
            # if fix_cross_experimental is starting this frame...
            if fix_cross_experimental.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross_experimental.frameNStart = frameN  # exact frame index
                fix_cross_experimental.tStart = t  # local t and not account for scr refresh
                fix_cross_experimental.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross_experimental, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_cross_experimental.started')
                # update status
                fix_cross_experimental.status = STARTED
                fix_cross_experimental.setAutoDraw(True)
            
            # if fix_cross_experimental is active this frame...
            if fix_cross_experimental.status == STARTED:
                # update params
                pass
            
            # if fix_cross_experimental is stopping this frame...
            if fix_cross_experimental.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_cross_experimental.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_cross_experimental.tStop = t  # not accounting for scr refresh
                    fix_cross_experimental.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_cross_experimental.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_cross_experimental.stopped')
                    # update status
                    fix_cross_experimental.status = FINISHED
                    fix_cross_experimental.setAutoDraw(False)
            
            # *palabra_experimental_text* updates
            
            # if palabra_experimental_text is starting this frame...
            if palabra_experimental_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                palabra_experimental_text.frameNStart = frameN  # exact frame index
                palabra_experimental_text.tStart = t  # local t and not account for scr refresh
                palabra_experimental_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(palabra_experimental_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'palabra_experimental_text.started')
                # update status
                palabra_experimental_text.status = STARTED
                palabra_experimental_text.setAutoDraw(True)
            
            # if palabra_experimental_text is active this frame...
            if palabra_experimental_text.status == STARTED:
                # update params
                pass
            
            # if palabra_experimental_text is stopping this frame...
            if palabra_experimental_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > palabra_experimental_text.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    palabra_experimental_text.tStop = t  # not accounting for scr refresh
                    palabra_experimental_text.tStopRefresh = tThisFlipGlobal  # on global time
                    palabra_experimental_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'palabra_experimental_text.stopped')
                    # update status
                    palabra_experimental_text.status = FINISHED
                    palabra_experimental_text.setAutoDraw(False)
            
            # *key_resp_4* updates
            waitOnFlip = False
            
            # if key_resp_4 is starting this frame...
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                # update status
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_4 is stopping this frame...
            if key_resp_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_4.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_4.tStop = t  # not accounting for scr refresh
                    key_resp_4.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                    # update status
                    key_resp_4.status = FINISHED
                    key_resp_4.status = FINISHED
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['a','s','k','l'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_4.keys == str(tecla_correcta)) or (key_resp_4.keys == tecla_correcta):
                        key_resp_4.corr = 1
                    else:
                        key_resp_4.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=experimental,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                experimental.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if experimental.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in experimental.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "experimental" ---
        for thisComponent in experimental.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for experimental
        experimental.tStop = globalClock.getTime(format='float')
        experimental.tStopRefresh = tThisFlipGlobal
        thisExp.addData('experimental.stopped', experimental.tStop)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
            # was no response the correct answer?!
            if str(tecla_correcta).lower() == 'none':
               key_resp_4.corr = 1;  # correct non-response
            else:
               key_resp_4.corr = 0;  # failed to respond (incorrectly)
        # store data for loop_experimental_stroop (TrialHandler)
        loop_experimental_stroop.addData('key_resp_4.keys',key_resp_4.keys)
        loop_experimental_stroop.addData('key_resp_4.corr', key_resp_4.corr)
        if key_resp_4.keys != None:  # we had a response
            loop_experimental_stroop.addData('key_resp_4.rt', key_resp_4.rt)
            loop_experimental_stroop.addData('key_resp_4.duration', key_resp_4.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if experimental.maxDurationReached:
            routineTimer.addTime(-experimental.maxDuration)
        elif experimental.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[ITI_text],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = None
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ITI" ---
        thisExp.currentRoutine = ITI
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # if trial has changed, end Routine now
            if hasattr(thisLoop_experimental_stroop, 'status') and thisLoop_experimental_stroop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_text* updates
            
            # if ITI_text is starting this frame...
            if ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_text.frameNStart = frameN  # exact frame index
                ITI_text.tStart = t  # local t and not account for scr refresh
                ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_text.started')
                # update status
                ITI_text.status = STARTED
                ITI_text.setAutoDraw(True)
            
            # if ITI_text is active this frame...
            if ITI_text.status == STARTED:
                # update params
                pass
            
            # if ITI_text is stopping this frame...
            if ITI_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_text.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_text.tStop = t  # not accounting for scr refresh
                    ITI_text.tStopRefresh = tThisFlipGlobal  # on global time
                    ITI_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_text.stopped')
                    # update status
                    ITI_text.status = FINISHED
                    ITI_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=ITI,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                ITI.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if ITI.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ITI.maxDurationReached:
            routineTimer.addTime(-ITI.maxDuration)
        elif ITI.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        # mark thisLoop_experimental_stroop as finished
        if hasattr(thisLoop_experimental_stroop, 'status'):
            thisLoop_experimental_stroop.status = FINISHED
        # if awaiting a pause, pause now
        if loop_experimental_stroop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            loop_experimental_stroop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'loop_experimental_stroop'
    loop_experimental_stroop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "fin_experimento" ---
    # create an object to store info about Routine fin_experimento
    fin_experimento = data.Routine(
        name='fin_experimento',
        components=[fin_experimento_image],
    )
    fin_experimento.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for fin_experimento
    fin_experimento.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    fin_experimento.tStart = globalClock.getTime(format='float')
    fin_experimento.status = STARTED
    thisExp.addData('fin_experimento.started', fin_experimento.tStart)
    fin_experimento.maxDuration = None
    # keep track of which components have finished
    fin_experimentoComponents = fin_experimento.components
    for thisComponent in fin_experimento.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fin_experimento" ---
    thisExp.currentRoutine = fin_experimento
    fin_experimento.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fin_experimento_image* updates
        
        # if fin_experimento_image is starting this frame...
        if fin_experimento_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fin_experimento_image.frameNStart = frameN  # exact frame index
            fin_experimento_image.tStart = t  # local t and not account for scr refresh
            fin_experimento_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fin_experimento_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fin_experimento_image.started')
            # update status
            fin_experimento_image.status = STARTED
            fin_experimento_image.setAutoDraw(True)
        
        # if fin_experimento_image is active this frame...
        if fin_experimento_image.status == STARTED:
            # update params
            pass
        
        # if fin_experimento_image is stopping this frame...
        if fin_experimento_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fin_experimento_image.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                fin_experimento_image.tStop = t  # not accounting for scr refresh
                fin_experimento_image.tStopRefresh = tThisFlipGlobal  # on global time
                fin_experimento_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fin_experimento_image.stopped')
                # update status
                fin_experimento_image.status = FINISHED
                fin_experimento_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=fin_experimento,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            fin_experimento.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if fin_experimento.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in fin_experimento.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fin_experimento" ---
    for thisComponent in fin_experimento.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for fin_experimento
    fin_experimento.tStop = globalClock.getTime(format='float')
    fin_experimento.tStopRefresh = tThisFlipGlobal
    thisExp.addData('fin_experimento.stopped', fin_experimento.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if fin_experimento.maxDurationReached:
        routineTimer.addTime(-fin_experimento.maxDuration)
    elif fin_experimento.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)

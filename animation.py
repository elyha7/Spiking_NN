import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import math
global_j=0
global_jmax=0
global_step = 25
def animate_weights(G,P,StateMonitorS,n_hidden,end=10000,start=0,save=True,show=True,step = 25):
    """
    show(bool) : whether to show
    save(bool) : whether to save
    start(int) : start tick
    end(int) : end tick
    P,G : Neuron groups. Visualising weights from P to G
    StateMonitorS : brian state monitor adjusted to weights you want to visualise
    global_step(int) :global ticks from frame to next frame
    global_j(int) : global counter
    global_jmax : global, set to math.floor((end-start)/global_step) inside
    """
    #step = 25
    global global_step
    global_step = step
    def frames_generator(G,P,StateMonitorS,n_hidden,step=global_step,end=10000,start=0):
        '''
        generator for speed(hope it helps)
        '''
        #Reshape all weights as input images and put them all into one array.
        toanim = []
        frame = start
        while frame < end:#in range(start,end,step):
            images_input = [[StateMonitorS.w[r + j * int(len(G))][frame]
                     for j in range(len(P))] 
                     for r in range(len(G))]
            images_input = np.array(images_input).reshape(int(n_hidden), int(n_input_width), int(n_input_height))
            together = np.hstack((images_input[0],np.ones((images_input[0].shape[0],1))*(np.nan),images_input[1],np.zeros((images_input[0].shape[0],1))*(np.nan),images_input[2]))
            #toanim.append(together)
            frame+=step
            #if frame>
            yield together


    #Create animation
    
    #%matplotlib osx
    global_j=0
    global global_jmax
    global_jmax = math.floor((end-start)/global_step)
    def generate_data():
        """
        awful piece of code
        """
        #global toanim
        global global_step
        global global_j
        global global_jmax
        global_j+=1
        if global_j>global_jmax:
            global_j=global_jmax
        for pic in frames_generator(G,P,StateMonitorS,step=global_step,end=end,start=global_j*global_step):
            break
        return pic#.reshape((8,8)) 

    def update(data):
        mat.set_data(data)
        return mat 

    #def data_gen():
    #    while True:
    #        yield frames_generator(G,P,StateMonitorS,step=25,end=10000,start=0)

    fig, ax = plt.subplots()
    mat = ax.imshow(generate_data(),cmap="winter",interpolation="none")
    plt.colorbar(mat)
    ani = animation.FuncAnimation(fig, update, frames_generator(G,P,StateMonitorS,step=global_step,end=end,start=start), interval=10,
                                  save_count=399)
    #Show animation
    if show:
        plt.show()
    if save:
        #Saving animation as mp4 file
        ani.save('MaWheightsAnimation.mp4',writer=animation.FFMpegFileWriter())

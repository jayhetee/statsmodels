import numpy as np

cov_params = np.array([ .00009333293468, 
                        5.611937227e-07, 
                        6.205446866e-07, 
                        4.556516622e-06, 
                       -9.822757384e-06, 
                       -2.031483395e-06, 
                       -1.500343113e-06, 
                       -2.307179219e-06, 
                       -.00034611970318, 
                       -2.269068240e-06, 
                        5.611937227e-07, 
                        9.578655751e-06, 
                       -8.283008266e-06, 
                        1.154577859e-06, 
                       -1.067225642e-06, 
                       -3.406126104e-06, 
                       -1.348425299e-06, 
                       -1.094550582e-06, 
                       -.00014811900567, 
                       -1.706419892e-07, 
                        6.205446866e-07, 
                       -8.283008266e-06, 
                        .00001109513991, 
                       -.00001610754441, 
                        4.397217669e-08, 
                        3.361139243e-06, 
                       -4.884097879e-07, 
                       -2.844813509e-07, 
                        .00011577311926, 
                       -3.311239816e-08, 
                        4.556516622e-06, 
                        1.154577859e-06, 
                       -.00001610754441, 
                        .00010136446733, 
                       -7.680511879e-06, 
                        2.751303907e-06, 
                        4.541099725e-06, 
                       -7.529105630e-07, 
                       -.00008187515419, 
                        4.119271028e-08, 
                       -9.822757384e-06, 
                       -1.067225642e-06, 
                        4.397217669e-08, 
                       -7.680511879e-06, 
                        .00011087912393, 
                       -1.634329824e-06, 
                       -1.951892115e-06, 
                        2.224577947e-06, 
                        -.0001663049582, 
                       -8.806187381e-07, 
                       -2.031483395e-06, 
                       -3.406126104e-06, 
                        3.361139243e-06, 
                        2.751303907e-06, 
                       -1.634329824e-06, 
                        .00002250087646, 
                       -.00001703962136, 
                       -4.023854993e-06, 
                       -.00016867618457, 
                       -6.849648026e-08, 
                       -1.500343113e-06, 
                       -1.348425299e-06, 
                       -4.884097879e-07, 
                        4.541099725e-06, 
                       -1.951892115e-06, 
                       -.00001703962136, 
                        .00011236581799, 
                       -9.676713547e-06, 
                       -.00005696461124, 
                        5.474876554e-07, 
                       -2.307179219e-06, 
                       -1.094550582e-06, 
                       -2.844813509e-07, 
                       -7.529105630e-07, 
                        2.224577947e-06, 
                       -4.023854993e-06, 
                       -9.676713547e-06, 
                        .00004927860288, 
                       -.00005986504882, 
                        4.053301953e-08, 
                       -.00034611970318, 
                       -.00014811900567, 
                        .00011577311926, 
                       -.00008187515419, 
                        -.0001663049582, 
                       -.00016867618457, 
                       -.00005696461124, 
                       -.00005986504882, 
                        .00811678179489, 
                        .00001891832827, 
                       -2.269068240e-06, 
                       -1.706419892e-07, 
                       -3.311239816e-08, 
                        4.119271028e-08, 
                       -8.806187381e-07, 
                       -6.849648026e-08, 
                        5.474876554e-07, 
                        4.053301953e-08, 
                        .00001891832827, 
                         .0000494330627]).reshape(10,10)

llf = np.array([ -7157.235602718])

llnull = np.array([-7500.3529693679])

n_lcens = np.array([               0])

n_rcens = np.array([             690])

n_ucens = np.array([            5676])

chi2 = np.array([ 686.23473329981])

df_model = np.array([               8])

df_resid = np.array([            6358])

params = np.array([-.22170886258436, 
                   -.01456977470549, 
                    .01196612919633, 
                   -.00781134201372, 
                   -.10133944575341, 
                   -.00978699834969, 
                    .04632503800812, 
                    .00261095348507, 
                    1.8650058597901, 
                    .72002443794028])

bse = np.array([ .00966089719825, 
                 .00309494034695, 
                 .00333093679178, 
                 .01006799221946, 
                 .01052991566607, 
                 .00474350887605, 
                 .01060027442991, 
                 .00701987199887, 
                 .09009318395355, 
                   .007030865004])

class Bunch(dict):
    def __init__(self, **kw):
        dict.__init__(self, kw)
        self.__dict__  = self


results = Bunch(cov_params=cov_params, llf=llf, llnull=llnull, n_lcens=n_lcens, n_rcens=n_rcens, n_ucens=n_ucens, chi2=chi2, df_model=df_model, df_resid=df_resid, params=params, bse=bse, )

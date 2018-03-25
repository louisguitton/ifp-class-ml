from matplotlib import pyplot as plt
from helpers.data import df, column_details


def relationship_plot(x1, x2=None, x1_lim=None, x2_lim=None):
    if x2:
        fig, ax = plt.subplots(3, 2, sharex='col', sharey='row', figsize=(15, 12))
        fig.subplots_adjust(hspace=0.1, wspace=0.1)

        df.plot(kind='scatter', x=x1, y='electricity-kWh', ax=ax[0, 0], c='g')
        df.plot(kind='scatter', x=x2, y='electricity-kWh', ax=ax[0, 1], c='g')
        df.plot(kind='scatter', x=x1, y='chilledWater-TonDays', ax=ax[1, 0], c='b')
        df.plot(kind='scatter', x=x2, y='chilledWater-TonDays', ax=ax[1, 1], c='b')
        df.plot(kind='scatter', x=x1, y='steam-LBS', ax=ax[2, 0], c='r')
        df.plot(kind='scatter', x=x2, y='steam-LBS', ax=ax[2, 1], c='r')

        for i in range(3):
            ax[i, 0].tick_params(which=u'major', reset=False, axis='y', labelsize=13)

        for i in range(2):
            ax[2, i].tick_params(which=u'major', reset=False, axis='x', labelsize=13)

        ax[2, 0].set_xlabel(x1, fontsize=13)
        ax[0, 0].set_title('Daily energy use versus {}'.format(x1), fontsize=15)
        ax[2, 0].set_xlim(x1_lim)

        ax[2, 1].set_xlabel(x2, fontsize=13)
        ax[0, 1].set_title('Daily energy use versus {}'.format(x2), fontsize=15)
        ax[2, 1].set_xlim(x2_lim)

        plt.show()
    else:
        fig, ax = plt.subplots(3, 1, sharex='col', figsize=(8, 12))
        fig.subplots_adjust(hspace=0.1, wspace=0.15)

        df.plot(kind='scatter', x=x1, y='electricity-kWh', ax=ax[0], c='g')
        df.plot(kind='scatter', x=x1, y='chilledWater-TonDays', ax=ax[1], c='b')
        df.plot(kind='scatter', x=x1, y='steam-LBS', ax=ax[2], c='r')

        for i in range(3):
            ax[i].tick_params(which=u'major', reset=False, axis='y', labelsize=13)

        ax[2].tick_params(which=u'major', reset=False, axis='x', labelsize=13)

        ax[2].set_xlabel(x1, fontsize=13)
        ax[0].set_title('Daily energy use versus {}'.format(x1), fontsize=15)

        plt.show()

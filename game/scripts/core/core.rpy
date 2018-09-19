init -2 python:
    class KeepRefs(object):
        __refs__ = defaultdict(list)
        def __init__(self):
            self.__refs__[self.__class__].append(weakref.ref(self))
        
        @classmethod
        def get_instances(cls):
            for inst_ref in cls.__refs__[cls]:
                inst = inst_ref()
                if inst is not None:
                    yield inst

    class LastUpdatedOrderedDict(OrderedDict):
        'Store items in the order the keys were last added'
        def __setitem__(self, key, value):
            if key in self:
                del self[key]
            OrderedDict.__setitem__(self, key, value)
        
        @property
        def listkeys(self):
            return list(self.keys())
        
        @property
        def listvalues(self):
            return list(self.values())
        
        @property
        def lastkey(self):
            return self.listkeys[-1]
        
        @property
        def lastvalue(self):
            return self.listvalues[-1]
        
        @property
        def isempty(self):
            return len(self.listkeys) == 0

    def format_seconds_to_dhm(seconds):
        """
            returns a string in the format : (x)d (y)h (z)m
        """
        string_to_format = '{}d, {}h, {}m'
        seconds = float(seconds)
        days = int(seconds / float(60*60*24))
        seconds -= days * (60*60*24)
        hours = int(seconds / float(60*60))
        seconds -= hours * (60*60)
        minutes = int(seconds / 60.0)
        return string_to_format.format(days, hours, minutes)

    def get_label(machine, location, state, variable=None):
        if variable is None:
            return "_".join(str(location), str(machine), str(state))
        else:
            return "_".join(str(location), str(machine), str(state), variable)

    def Sleep():
        global game
        try:
            game.sleep()
        except OnSleepException:
            renpy.jump("sleeping_locked")
        
        for event in store.my_events:
            event.complete_events()
        
        global aunt_dialogue_advance
        global aunt_count
        global sis_bedroom_count
        global diary_scene
        global erik_drunk
        global training_done
        global mrsj_filled
        global erik_funky
        global orcette_mail_lock
        global M_jenny
        
        if aunt_dialogue_advance:
            aunt_dialogue_advance = False
            aunt_count += 1
        M_jenny.unforce()
        diary_scene = False
        erik_drunk = False
        training_done = False
        mrsj_filled = False
        erik_funky = False
        if game.timer.dayOfWeek() == "Tue" and erik.completed(erik_orcette):
            orcette_mail_lock = True

    def randomizer(name = "", start = 0, end = 99):
        rand = renpy.random.randint(start, end)
        if name == "":
            return rand
        if not re.search('\{}', name):
            name = name + '{}'
        tmp = name.format(rand)
        return tmp

    def choice_randomizer(list):
        r = random.uniform(0, sum([v[1] for v in list]))
        s = 0.0
        for k, w in list:
            s += w
            if r < s:
                return k
        return k

    def progressCamShow(nextCamShow):
        current_camshow = nextCamShow

    def get_returnable_books():
        if player.has_item("french_dictionary") and player.has_item("french_love") and M_bissette.is_state(S_bissette_end):
            return True
        if player.has_item("old_book") and M_aqua.is_state((S_aqua_trade, S_aqua_fishing, S_aqua_chase,
                   S_aqua_squid_gaurd, S_aqua_maze, S_aqua_lair, S_aqua_found,
                   S_aqua_mating_proposal, S_aqua_valor_test, S_aqua_mate,
                   S_aqua_seasucc_intro, S_aqua_seasucc_mushroom, S_aqua_end)):
            return True
        return False

    def insert_newlines(string, every=30):
        lines = []
        for i in xrange(0, len(string), every):
            lines.append(string[i:i+every])
        return '\n'.join(lines)

    def text_identity(text):
        return text

    class Quest:
        def __init__(self, name, image="", status= False):
            self.name = name
            self.image = image
            self.status = status

    def quest_complete(Quest):
        completed_quests.append(Quest)

    def clamp(number, lower, upper):
        assert lower < upper, "Error in clamp call, lower bound is greater than upper bound"
        return lower if number < lower else upper if number > upper else number

    def gauss(mean, deviation, lower, upper):
        return int(clamp(random.gauss(mean, deviation), lower, upper))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

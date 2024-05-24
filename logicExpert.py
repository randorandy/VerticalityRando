from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places. 
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Bombs, HiJump,
    Varia, GravitySuit, Wave, SpeedBooster, Spazer, Ice, Grapple,
    Plasma, Screw, SpaceJump, Energy, Reserve,
    Glider, ChargeMissile, ReserveMissile, Overcharge, ChargeSuper
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 1
))

energy300 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 14
))
hellrun1 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy200 in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy500 in loadout)
))
hellrun5 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))
hellrun7 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))


missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 4 >= 10
))
missile20 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 4 >= 20
))

super4 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 4
))
super6 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 6
))
super12 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 12
))
super30 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 2 >= 30
))
powerBomb4 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 2
))
powerBomb6 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 3
))
powerBomb8 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 4
))
powerBomb10 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 5
))
powerBomb12 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 6
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (
        (canUseBombs in loadout) or
        (Screw in loadout)
    ) and
    (Morph in loadout)
    #but in this hack the first item is morph
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (Missile in loadout) or
        (Super in loadout)
        )
))
greenDoor = LogicShortcut(lambda loadout: (
    (Super in loadout) or
    (
        (Missile in loadout) and
        (ChargeMissile in loadout)
    )
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canSBJ = LogicShortcut(lambda loadout: (
    (HiJump in loadout) and
    (Morph in loadout)
))
canFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout)
))
canSpeedOrFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout) or
    (SpeedBooster in loadout)
))
canHop = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) or
    (
        (Morph in loadout) and
        (HiJump in loadout)
    )
))

draygonArea = LogicShortcut(lambda loadout: (
    (canBreakBlocks in loadout) and
    (pinkDoor in loadout) and
    (
        (
            (canUsePB in loadout) and
            (
                (GravitySuit in loadout) or
                (HiJump in loadout)
            )
        ) or
        (
            (GravitySuit in loadout) and
            (SpeedBooster in loadout)
        )
    )
     
))
brinstar = LogicShortcut(lambda loadout: (
    (canBreakBlocks in loadout) and
    (greenDoor in loadout) and
    (
        (Glider in loadout) or
        (SpaceJump in loadout)
    )
))
upperBrinstar = LogicShortcut(lambda loadout: (
    (brinstar in loadout) and
    (Wave in loadout) and
    (
        (Grapple in loadout) or
        (Glider in loadout) or
        (canFly in loadout) 
    )
))
wreckedShip = LogicShortcut(lambda loadout: (
    (upperBrinstar in loadout) and
    (SpeedBooster in loadout)
))
upperShip = LogicShortcut(lambda loadout: (
    (wreckedShip in loadout) and
    (canUsePB in loadout)
))
crateria = LogicShortcut(lambda loadout: (
    (upperShip in loadout) and
    (SpaceJump in loadout)
))

allItems = LogicShortcut(lambda loadout: (
    (Missile in loadout) and
    (super12 in loadout) and
    (PowerBomb in loadout) and
    (Morph in loadout) and
    (Grapple in loadout) and
    (Bombs in loadout) and
    (HiJump in loadout) and
    (GravitySuit in loadout) and
    (Varia in loadout) and
    (Wave in loadout) and
    (SpeedBooster in loadout) and
    (Spazer in loadout) and
    (Ice in loadout) and
    (Plasma in loadout) and
    (Screw in loadout) and
    (SpaceJump in loadout) and
    (Glider in loadout) and
    (ChargeMissile in loadout) and
    (ReserveMissile in loadout) and
    (ChargeSuper in loadout)
))


area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


location_logic: LocationLogicType = {
    "Morph Ball 43": lambda loadout: (
        True #But has a special case
    ),
    "Alpha Missile 44": lambda loadout: (
        (Morph in loadout)
    ),
    "Bombs 46": lambda loadout: (
        (Missile in loadout) and
        (canBreakBlocks in loadout)
    ),
    "First Energy Tank 42": lambda loadout: (
        (canBreakBlocks in loadout)
    ),
    "Missile 47": lambda loadout: (
        (canBreakBlocks in loadout)
    ),
    "Missile 45": lambda loadout: (
        (Missile in loadout)
    ),
    "Reserve Missile 51": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout)
    ),
    "Missile 93": lambda loadout: (
        (draygonArea in loadout) and
        (
            (GravitySuit in loadout) or
            (Grapple in loadout)
        )
    ),
    "Missile 76": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout)
    ),
    "Energy Tank 77": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout)
    ),
    "Spazer 78": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout)
    ),
    "Missile 79": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout)
    ),
    "HiJump 80": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout)
    ),
    "Power Bomb 84": lambda loadout: (
        (canUsePB in loadout) and
        (pinkDoor in loadout)
    ),
    "Missile 88": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout)
    ),
    "Energy Tank 90": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout) and
        (Glider in loadout)
    ),
    "Missile 48": lambda loadout: (
        (canUseBombs in loadout) and
        (pinkDoor in loadout)
    ),
    "Reserve Tank 52": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout) and
        (Varia in loadout) #hellrun?
    ),
    "Missile 54": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout) and
        (Varia in loadout) and
        (Glider in loadout)
    ),
    "Missile 55": lambda loadout: (
        (canUseBombs in loadout) and
        (pinkDoor in loadout) and
        (Varia in loadout)
    ),
    "Missile 86": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout) and
        (
            (Varia in loadout) or
            (greenDoor in loadout)
        )
    ),
    "Energy Tank 91": lambda loadout: (
        (draygonArea in loadout)
    ),
    "Power Bomb 95": lambda loadout: (
        (draygonArea in loadout) and
        (canUsePB in loadout) and
        (
            (GravitySuit in loadout) or
            (Grapple in loadout)
        )
    ),
    "Missile 92": lambda loadout: (
        (draygonArea in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Power Bomb 94": lambda loadout: (
        (draygonArea in loadout) and
        (
            (canUsePB in loadout) or
            (
                (GravitySuit in loadout) and
                (Glider in loadout)
            )
        ) and
        (energy400 in loadout)
    ),
    "Power Bomb 96": lambda loadout: (
        (draygonArea in loadout) and
        (canUsePB in loadout)
    ),
    "Super Missile 50": lambda loadout: (
        (canBreakBlocks in loadout) and
        (greenDoor in loadout) and
        (Varia in loadout)
    ),
    "Glider 81": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout)
    ),
    "Energy Tank 82": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout) and
        (Glider in loadout)
    ),
    "Varia Suit 85": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout) and
        (Glider in loadout) and
        (
            (Varia in loadout) or
            (greenDoor in loadout)
        )
    ),
    "Energy Tank 49": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout) and
        (Varia in loadout)
    ),
    "Power Bomb 21": lambda loadout: (
        (brinstar in loadout) and
        (canUsePB in loadout)
    ),
    "Energy Tank 20": lambda loadout: (
        (brinstar in loadout)
    ),
    "Reserve Missile 26": lambda loadout: (
        (brinstar in loadout) and
        (SpeedBooster in loadout)
    ),
    "Missile 23": lambda loadout: (
        (brinstar in loadout)
    ),
    "Super Missile 18": lambda loadout: (
        (brinstar in loadout)
    ),
    "Missile 24": lambda loadout: (
        (brinstar in loadout) and
        (
            (Glider in loadout) or
            (SpaceJump in loadout)
        )
    ),
    "Grapple Beam 25": lambda loadout: (
        (brinstar in loadout) and
        (
            (Grapple in loadout) or
            (Wave in loadout)
        )
    ),
    "Wave Beam 41": lambda loadout: (
        (brinstar in loadout) #more?
    ),
    "Missile 19": lambda loadout: (
        (upperBrinstar in loadout)
    ),
    "Missile 27": lambda loadout: (
        (upperBrinstar in loadout) and
        (
            (SpaceJump in loadout) or
            (Grapple in loadout) #maybe
        )
    ),
    "Missile 22": lambda loadout: (
        (upperBrinstar in loadout) and
        (canUseBombs in loadout) and
        (canHop in loadout)
    ),
    "Energy Tank 31": lambda loadout: (
        (upperBrinstar in loadout) and
        (SpeedBooster in loadout)
    ),
    "Missile 30": lambda loadout: (
        (upperBrinstar in loadout) and
        (SpeedBooster in loadout)
    ),
    "Missile 34": lambda loadout: (
        (brinstar in loadout)
    ),
    "Power Bomb 32": lambda loadout: (
        (brinstar in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ),
    "Missile 28": lambda loadout: (
        (brinstar in loadout) and
        (
            (SpaceJump in loadout) or
            (Glider in loadout)
        )
    ),
    "Speed Booster 36": lambda loadout: (
        (upperBrinstar in loadout)
    ),
    "Missile 61": lambda loadout: (
        (wreckedShip in loadout) and
        (SpeedBooster in loadout)
    ),
    "Missile 62": lambda loadout: (
        (wreckedShip in loadout) and
        (SpeedBooster in loadout)
    ),
    "Energy Tank 63": lambda loadout: (
        (wreckedShip in loadout)
    ),
    "Ice Beam 64": lambda loadout: (
        (wreckedShip in loadout) and
        (
            (Glider in loadout) or
            (SpaceJump in loadout)
        )
    ),
    "Missile 58": lambda loadout: (
        (wreckedShip in loadout) and
        (SpeedBooster in loadout)
    ),
    "Reserve Tank 59": lambda loadout: (
        (wreckedShip in loadout) and
        (SpeedBooster in loadout)
    ),
    "Super Missile 65": lambda loadout: (
        (upperBrinstar in loadout) #though it's in ws
    ),
    "Energy Tank 70": lambda loadout: (
        (upperShip in loadout)
    ),
    "Power Bomb 71": lambda loadout: (
        (upperShip in loadout) and
        (SpeedBooster in loadout)
    ),
    "Energy Tank 72": lambda loadout: (
        (upperShip in loadout)
    ),
    "Space Jump 75": lambda loadout: (
        (upperShip in loadout) and
        (canFly in loadout)
    ),
    "Missile 3": lambda loadout: (
        (crateria in loadout)
    ),
    "Plasma Beam 4": lambda loadout: (
        (crateria in loadout)
    ),
    "Power Bomb 5": lambda loadout: (
        (crateria in loadout) and
        (SpeedBooster in loadout)
    ),
    "Missile 6": lambda loadout: (
        (crateria in loadout)
    ),
    "Power Bomb 12": lambda loadout: (
        (crateria in loadout) and
        (SpeedBooster in loadout)
    ),
    "Screw Attack 10": lambda loadout: (
        (crateria in loadout) and
        (Plasma in loadout) and
        (energy600 in loadout) 
    ),
    "Super Missile 14": lambda loadout: (
        (crateria in loadout) and
        (Plasma in loadout) and
        (energy600 in loadout) and
        (Screw in loadout) #could be better due to gray door
    ),
    "Missile 8": lambda loadout: (
        (crateria in loadout)
    ),
    "Energy Tank 0": lambda loadout: (
        (crateria in loadout)
    ),
    "Super Missile 2": lambda loadout: (
        (crateria in loadout) and
        (Screw in loadout)
    ),
    "Reserve Tank 1": lambda loadout: (
        (crateria in loadout) and
        (Screw in loadout)
    ),
    "Reserve Missile 7": lambda loadout: (
        (crateria in loadout)
    ),
    "Missile 15": lambda loadout: (
        (crateria in loadout)
    ),
    "Missile 11": lambda loadout: (
        (crateria in loadout)
    ),
    "Energy Tank 73": lambda loadout: (
        (upperShip in loadout) and
        (SpaceJump in loadout)
    ),
    "Super Missile 74": lambda loadout: (
        (upperShip in loadout) and
        (SpaceJump in loadout)
    ),
    "Power Bomb 60": lambda loadout: (
        (upperShip in loadout)
    ),
    "Missile 66": lambda loadout: (
        (wreckedShip in loadout)
    ),
    "Reserve Missile 67": lambda loadout: (
        (wreckedShip in loadout) and
        (SpaceJump in loadout)
    ),
    "Gravity Suit 69": lambda loadout: (
        (wreckedShip in loadout) and
        (GravitySuit in loadout)
    ),
    "Super Missile 40": lambda loadout: (
        (upperBrinstar in loadout) and
        (Grapple in loadout) and
        (SpeedBooster in loadout)
    ),
    "Missile 38": lambda loadout: (
        (upperBrinstar in loadout)
    ),
    "Super Missile 39": lambda loadout: (
        (upperBrinstar in loadout) and
        (SpeedBooster in loadout)
    ),
    "Reserve Tank 33": lambda loadout: (
        (upperBrinstar in loadout) and
        (Grapple in loadout) and #maybe?
        (SpeedBooster in loadout)
    ),
    "Missile 29": lambda loadout: (
        (upperBrinstar in loadout)
    ),
    "Missile 35": lambda loadout: (
        (upperBrinstar in loadout)
    ),
    "Charge Missile 255": lambda loadout: (
        (upperBrinstar in loadout) and
        (Glider in loadout) #more?
    ),
    "Missile 37": lambda loadout: (
        (brinstar in loadout)
    ),
    "Missile 16": lambda loadout: (
        (upperBrinstar in loadout)
    ),
    "Super Missile 17": lambda loadout: (
        (upperBrinstar in loadout)
    ),
    "Missile 57": lambda loadout: (
        (canBreakBlocks in loadout) and
        (pinkDoor in loadout) and
        (Varia in loadout)
    ),
    "Missile 68": lambda loadout: (
        (wreckedShip in loadout)
    ),
    "Super Missile 56": lambda loadout: (
        (canUseBombs in loadout) and
        (greenDoor in loadout) and
        (Varia in loadout) and
        (SpaceJump in loadout) #maybe other ways?
    ),
    "Missile 89": lambda loadout: (
        (canBreakBlocks in loadout) and
        (greenDoor in loadout)
    ),
    "Missile 87": lambda loadout: (
        (brinstar in loadout) #basically brinstar though it's maridia
    ),
    "Missile 83": lambda loadout: (
        (canUseBombs in loadout) and
        (pinkDoor in loadout) and
        (
            (greenDoor in loadout) or
            (
                (Glider in loadout) and
                (Varia in loadout)
            )
        )
    ),
    "Charge Missile 254": lambda loadout: (
        (draygonArea in loadout) and
        (canUsePB in loadout) and
        (
            (GravitySuit in loadout) or
            (Grapple in loadout)
        ) and
        (greenDoor in loadout)
    ),
    "Missile 13": lambda loadout: (
        (upperBrinstar in loadout)
    ),
    "Overcharge 53": lambda loadout: (
        (canUseBombs in loadout) and
        (pinkDoor in loadout) and
        (Varia in loadout)
    ),
    "Energy Tank 9": lambda loadout: (
        (crateria in loadout) and
        (Screw in loadout)
    ),

}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True

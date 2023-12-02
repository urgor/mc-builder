class Block:
    """Minecraft PI block description. Can be sent to Minecraft.setBlock/s"""
    def __init__(self, id, data=0):
        self.id = id
        self.data = data

    def __cmp__(self, rhs):
        return hash(self) - hash(rhs)

    def __eq__(self, rhs):
        return self.id == rhs.id and self.data == rhs.data

    def __hash__(self):
        return (self.id << 8) + self.data

    def withData(self, data):
        return Block(self.id, data)

    def __iter__(self):
        """Allows a Block to be sent whenever id [and data] is needed"""
        return iter((self.id, self.data))
        
    def __repr__(self):
        return "Block(%d, %d)"%(self.id, self.data)

# Ported from page https://minecraft-ids.grahamedgecombe.com/
# Minecraft version 1.20.x

COLOR_WHITE = 0
COLOR_ORANGE = 1
COLOR_MAGENTA = 2
COLOR_LIGHT_BLUE = 3
COLOR_YELLOW = 4
COLOR_LIME = 5
COLOR_PINK = 6
COLOR_GRAY = 7
COLOR_LIGHT_GRAY = 8
COLOR_CYAN = 9
COLOR_PURPLE = 10
COLOR_BLUE = 11
COLOR_BROWN = 12
COLOR_GREEN = 13
COLOR_RED = 14
COLOR_BLACK = 15

AIR = Block(0)
STONE = Block(1)
GRANITE = Block(1, 1)
GRANITE_POLISHED = Block(1, 2)
DIORITE = Block(1, 3)
DIORITE_POLISHED = Block(1, 4)
ANDESITE = Block(1, 5)
ANDESITE_POLISHED = Block(1, 6)
GRASS = Block(2)
DIRT = Block(3)
DIRT_COARSE = Block(3, 1)
PODZOL = Block(3, 2)
COBBLESTONE = Block(4)
PLANKS_OAK_WOOD = Block(5)
PLANKS_SPRUCE_WOOD = Block(5, 1)
PLANKS_BIRCH_WOOD = Block(5, 2)
PLANKS_JUNGLE_WOOD = Block(5, 3)
PLANKS_ACACIA_WOOD = Block(5, 4)
PLANKS_DARK_OAK = Block(5, 5)
SAPLING_OAK = Block(6)
SAPLING_SPRUCE = Block(6, 1)
SAPLING_BIRCH = Block(6, 2)
SAPLING_JUNGLE = Block(6, 3)
SAPLING_ACACIA = Block(6, 4)
SAPLING_DARK_OAK = Block(6, 5)
BEDROCK = Block(7)
WATER_FLOWING = Block(8)
WATER_STILL = Block(9)
LAVA_FLOWING = Block(10)
LAVA_STILL = Block(11)
SAND = Block(12)
SAND_RED = Block(12, 1)
GRAVEL = Block(13)
ORE_GOLD = Block(14)
ORE_IRON = Block(15)
ORE_COAL = Block(16)
LOG_OAK = Block(17)
LOG_SPRUCE = Block(17, 1)
LOG_BIRCH = Block(17, 2)
LOG_JUNGLE = Block(17, 3)
LEAVES_OAK = Block(18)
LEAVES_SPRUCE = Block(18, 1)
LEAVES_BIRCH = Block(18, 2)
LEAVES_JUNGLE = Block(18, 3)
SPONGE = Block(19)
SPONGE_WET = Block(19, 1)
GLASS = Block(20)
ORE_LAPIS = Block(21)
BLOCK_LAPIS = Block(22)
DISPENSER = Block(23)
SANDSTONE = Block(24)
SANDSTONE_CHISELED = Block(24, 1)
SANDSTONE_SMOOTH = Block(24, 2)
NOTEBLOCK = Block(25)
BED = Block(26)
RAIL_GOLDEN = Block(27)
RAIL_DETECTOR = Block(28)
STICKY_PISTON = Block(29)
WEB = Block(30)
TALLGRASS_DEAD_SHRUB = Block(31)
TALLGRASS_GRASS = Block(31, 1)
TALLGRASS_FERN = Block(31, 2)
DEADBUSH = Block(32)
PISTON = Block(33)
PISTON_HEAD = Block(34)
WOOL = Block(35)
WOOL_ORANGE = Block(35, COLOR_ORANGE)
WOOL_MAGENTA = Block(35, COLOR_MAGENTA)
WOOL_LIGHT_BLUE = Block(35, COLOR_LIGHT_BLUE)
WOOL_YELLOW = Block(35, COLOR_YELLOW)
WOOL_LIME = Block(35, COLOR_LIME)
WOOL_PINK = Block(35, COLOR_PINK)
WOOL_GRAY = Block(35, COLOR_GRAY)
WOOL_LIGHT_GRAY = Block(35, COLOR_LIGHT_GRAY)
WOOL_CYAN = Block(35, COLOR_CYAN)
WOOL_PURPLE = Block(35, COLOR_PURPLE)
WOOL_BLUE = Block(35, COLOR_BLUE)
WOOL_BROWN = Block(35, COLOR_BROWN)
WOOL_GREEN = Block(35, COLOR_GREEN)
WOOL_RED = Block(35, COLOR_RED)
WOOL_BLACK = Block(35, COLOR_BLACK)
YELLOW_FLOWER = Block(37)
FLOWER_POPPY = Block(38)
FLOWER_BLUE_ORCHID = Block(38, 1)
FLOWER_ALLIUM = Block(38, 2)
FLOWER_AZURE_BLUET = Block(38, 3)
FLOWER_RED_TULIP = Block(38, 4)
FLOWER_ORANGE_TULIP = Block(38, 5)
FLOWER_WHITE_TULIP = Block(38, 6)
FLOWER_PINK_TULIP = Block(38, 7)
FLOWER_OXEYE_DAISY = Block(38, 8)
MUSHROOM_BROWN = Block(39)
MUSHROOM_RED = Block(40)
BLOCK_GOLD = Block(41)
BLOCK_IRON = Block(42)
DOUBLE_STONE_SLAB = Block(43)
DOUBLE_SANDSTONE_SLAB = Block(43, 1)
DOUBLE_WOODEN_SLAB = Block(43, 2)
DOUBLE_COBBLESTONE_SLAB = Block(43, 3)
DOUBLE_BRICK_SLAB = Block(43, 4)
DOUBLE_STONE_BRICK_SLAB = Block(43, 5)
DOUBLE_NETHER_BRICK_SLAB = Block(43, 6)
DOUBLE_QUARTZ_SLAB = Block(43, 7)
STONE_SLAB = Block(44)
STONE_SLAB_SANDSTONE = Block(44, 1)
STONE_SLAB_WOODEN = Block(44, 2)
STONE_SLAB_COBBLESTONE = Block(44, 3)
STONE_SLAB_BRICK = Block(44, 4)
STONE_SLAB_STONE_BRICK = Block(44, 5)
STONE_SLAB_NETHER_BRICK = Block(44, 6)
STONE_SLAB_QUARTZ = Block(44, 7)
BLOCK_BRICK = Block(45)
TNT = Block(46)
BOOKSHELF = Block(47)
MOSSY_COBBLESTONE = Block(48)
OBSIDIAN = Block(49)
TORCH = Block(50)
FIRE = Block(51)
MOB_SPAWNER = Block(52)
OAK_STAIRS = Block(53)
CHEST = Block(54)
REDSTONE_WIRE = Block(55)
DIAMOND_ORE = Block(56)
DIAMOND_BLOCK = Block(57)
CRAFTING_TABLE = Block(58)
WHEAT_CROPS = Block(59)
FARMLAND = Block(60)
FURNACE = Block(61)
LIT_FURNACE = Block(62)
STANDING_SIGN = Block(63)
WOODEN_DOOR = Block(64)
LADDER = Block(65)
RAIL = Block(66)
STONE_STAIRS = Block(67)
WALL_SIGN = Block(68)
LEVER = Block(69)
STONE_PRESSURE_PLATE = Block(70)
IRON_DOOR_BLOCK = Block(71)
WOODEN_PRESSURE_PLATE = Block(72)
REDSTONE_ORE = Block(73)
LIT_REDSTONE_ORE = Block(74)
UNLIT_REDSTONE_TORCH = Block(75)
REDSTONE_TORCH = Block(76)
STONE_BUTTON = Block(77)
SNOW_LAYER = Block(78)
ICE = Block(79)
SNOW = Block(80)
CACTUS = Block(81)
CLAY = Block(82)
REEDS = Block(83)
JUKEBOX = Block(84)
FENCE = Block(85)
PUMPKIN = Block(86)
NETHERRACK = Block(87)
SOUL_SAND = Block(88)
GLOWSTONE = Block(89)
PORTAL = Block(90)
LIT_PUMPKIN = Block(91)
CAKE_BLOCK = Block(92)
UNPOWERED_REPEATER = Block(93)
POWERED_REPEATER = Block(94)
STAINED_GLASS_WHITE = Block(95, COLOR_WHITE)
STAINED_GLASS_ORANGE = Block(95, COLOR_ORANGE)
STAINED_GLASS_MAGENTA = Block(95, COLOR_MAGENTA)
STAINED_GLASS_LIGHT_BLUE = Block(95, COLOR_LIGHT_BLUE)
STAINED_GLASS_YELLOW = Block(95, COLOR_YELLOW)
STAINED_GLASS_LIME = Block(95, COLOR_LIME)
STAINED_GLASS_PINK = Block(95, COLOR_PINK)
STAINED_GLASS_GRAY = Block(95, COLOR_GRAY)
STAINED_GLASS_LIGHT_GRAY = Block(95, COLOR_LIGHT_GRAY)
STAINED_GLASS_CYAN = Block(95, COLOR_CYAN)
STAINED_GLASS_PURPLE = Block(95, COLOR_PURPLE)
STAINED_GLASS_BLUE = Block(95, COLOR_BLUE)
STAINED_GLASS_BROWN = Block(95, COLOR_BROWN)
STAINED_GLASS_GREEN = Block(95, COLOR_GREEN)
STAINED_GLASS_RED = Block(95, COLOR_RED)
STAINED_GLASS_BLACK = Block(95, COLOR_BLACK)
TRAPDOOR = Block(96)
MONSTER_EGG_STONE = Block(97)
MONSTER_EGG_COBBLESTONE = Block(97, 1)
MONSTER_EGG_STONE_BRICK = Block(97, 2)
MONSTER_EGG_MOSSY_STONE_BRICK = Block(97, 3)
MONSTER_EGG_CRACKED_STONE_BRICK = Block(97, 4)
MONSTER_EGG_CHISELED_STONE_BRICK = Block(97, 5)
STONEBRICK_STONE = Block(98)
STONEBRICK_MOSSY = Block(98, 1)
STONEBRICK_CRACKED = Block(98, 2)
STONEBRICK_CHISELED = Block(98, 3)
BROWN_MUSHROOM_BLOCK = Block(99)
RED_MUSHROOM_BLOCK = Block(100)
IRON_BARS = Block(101)
GLASS_PANE = Block(102)
MELON_BLOCK = Block(103)
PUMPKIN_STEM = Block(104)
MELON_STEM = Block(105)
VINE = Block(106)
FENCE_GATE = Block(107)
BRICK_STAIRS = Block(108)
STONE_BRICK_STAIRS = Block(109)
MYCELIUM = Block(110)
WATERLILY = Block(111)
NETHER_BRICK = Block(112)
NETHER_BRICK_FENCE = Block(113)
NETHER_BRICK_STAIRS = Block(114)
NETHER_WART = Block(115)
ENCHANTING_TABLE = Block(116)
BREWING_STAND = Block(117)
CAULDRON = Block(118)
END_PORTAL = Block(119)
END_PORTAL_FRAME = Block(120)
END_STONE = Block(121)
DRAGON_EGG = Block(122)
REDSTONE_LAMP = Block(123)
LIT_REDSTONE_LAMP = Block(124)
DOUBLE_WOODEN_SLAB_OAK = Block(125)
DOUBLE_WOODEN_SLAB_SPRUCE = Block(125, 1)
DOUBLE_WOODEN_SLAB_BIRCH = Block(125, 2)
DOUBLE_WOODEN_SLAB_JUNGLE = Block(125, 3)
DOUBLE_WOODEN_SLAB_ACACIA = Block(125, 4)
DOUBLE_WOODEN_SLAB_DARK_OAK = Block(125, 5)
WOODEN_SLAB_OAK = Block(126)
WOODEN_SLAB_SPRUCE = Block(126, 1)
WOODEN_SLAB_BIRCH = Block(126, 2)
WOODEN_SLAB_JUNGLE = Block(126, 3)
WOODEN_SLAB_ACACIA = Block(126, 4)
WOODEN_SLAB_DARK_OAK = Block(126, 5)
COCOA = Block(127)
SANDSTONE_STAIRS = Block(128)
EMERALD_ORE = Block(129)
ENDER_CHEST = Block(130)
TRIPWIRE_HOOK = Block(131)
TRIPWIRE = Block(132)
EMERALD_BLOCK = Block(133)
SPRUCE_STAIRS = Block(134)
BIRCH_STAIRS = Block(135)
JUNGLE_STAIRS = Block(136)
COMMAND_BLOCK = Block(137)
BEACON = Block(138)
COBBLESTONE_WALL = Block(139)
COBBLESTONE_WALL_MOSSY = Block(139, 1)
FLOWER_POT = Block(140)
CARROTS = Block(141)
POTATOES = Block(142)
WOODEN_BUTTON = Block(143)
SKULL = Block(144)
ANVIL = Block(145)
TRAPPED_CHEST = Block(146)
LIGHT_WEIGHTED_PRESSURE_PLATE = Block(147)
HEAVY_WEIGHTED_PRESSURE_PLATE = Block(148)
UNPOWERED_COMPARATOR = Block(149)
POWERED_COMPARATOR = Block(150)
DAYLIGHT_DETECTOR = Block(151)
REDSTONE_BLOCK = Block(152)
QUARTZ_ORE = Block(153)
HOPPER = Block(154)
QUARTZ_BLOCK = Block(155)
QUARTZ_BLOCK_CHISELED = Block(155, 1)
QUARTZ_BLOCK_PILLAR = Block(155, 2)
QUARTZ_STAIRS = Block(156)
ACTIVATOR_RAIL = Block(157)
DROPPER = Block(158)
STAINED_HARDENED_CLAY_WHITE = Block(159, COLOR_WHITE)
STAINED_HARDENED_CLAY_ORANGE = Block(159, COLOR_ORANGE)
STAINED_HARDENED_CLAY_MAGENTA = Block(159, COLOR_MAGENTA)
STAINED_HARDENED_CLAY_LIGHT_BLUE = Block(159, COLOR_LIGHT_BLUE)
STAINED_HARDENED_CLAY_YELLOW = Block(159, COLOR_YELLOW)
STAINED_HARDENED_CLAY_LIME = Block(159, COLOR_LIME)
STAINED_HARDENED_CLAY_PINK = Block(159, COLOR_PINK)
STAINED_HARDENED_CLAY_GRAY = Block(159, COLOR_GRAY)
STAINED_HARDENED_CLAY_LIGHT_GRAY = Block(159, COLOR_LIGHT_GRAY)
STAINED_HARDENED_CLAY_CYAN = Block(159, COLOR_CYAN)
STAINED_HARDENED_CLAY_PURPLE = Block(159, COLOR_PURPLE)
STAINED_HARDENED_CLAY_BLUE = Block(159, COLOR_BLUE)
STAINED_HARDENED_CLAY_BROWN = Block(159, COLOR_BROWN)
STAINED_HARDENED_CLAY_GREEN = Block(159, COLOR_GREEN)
STAINED_HARDENED_CLAY_RED = Block(159, COLOR_RED)
STAINED_HARDENED_CLAY_BLACK = Block(159, COLOR_BLACK)
STAINED_GLASS_PANE_WHITE = Block(160, COLOR_WHITE)
STAINED_GLASS_PANE_ORANGE = Block(160, COLOR_ORANGE)
STAINED_GLASS_PANE_MAGENTA = Block(160, COLOR_MAGENTA)
STAINED_GLASS_PANE_LIGHT_BLUE = Block(160, COLOR_LIGHT_BLUE)
STAINED_GLASS_PANE_YELLOW = Block(160, COLOR_YELLOW)
STAINED_GLASS_PANE_LIME = Block(160, COLOR_LIME)
STAINED_GLASS_PANE_PINK = Block(160, COLOR_PINK)
STAINED_GLASS_PANE_GRAY = Block(160, COLOR_GRAY)
STAINED_GLASS_PANE_LIGHT_GRAY = Block(160, COLOR_LIGHT_GRAY)
STAINED_GLASS_PANE_CYAN = Block(160, COLOR_CYAN)
STAINED_GLASS_PANE_PURPLE = Block(160, COLOR_PURPLE)
STAINED_GLASS_PANE_BLUE = Block(160, COLOR_BLUE)
STAINED_GLASS_PANE_BROWN = Block(160, COLOR_BROWN)
STAINED_GLASS_PANE_GREEN = Block(160, COLOR_GREEN)
STAINED_GLASS_PANE_RED = Block(160, COLOR_RED)
STAINED_GLASS_PANE_BLACK = Block(160, COLOR_BLACK)
LEAVES_ACACIA = Block(161)
LEAVES_DARK_OAK = Block(161, 1)
LOG_ACACIA = Block(162)
LOG_DARK_OAK = Block(162, 1)
ACACIA_STAIRS = Block(163)
DARK_OAK_STAIRS = Block(164)
SLIME = Block(165)
BARRIER = Block(166)
IRON_TRAPDOOR = Block(167)
PRISMARINE = Block(168)
PRISMARINE_BRICKS = Block(168, 1)
PRISMARINE_DARK = Block(168, 2)
SEA_LANTERN = Block(169)
HAY_BLOCK = Block(170)
CARPET_WHITE = Block(171, COLOR_WHITE)
CARPET_ORANGE = Block(171, COLOR_ORANGE)
CARPET_MAGENTA = Block(171, COLOR_MAGENTA)
CARPET_LIGHT_BLUE = Block(171, COLOR_LIGHT_BLUE)
CARPET_YELLOW = Block(171, COLOR_YELLOW)
CARPET_LIME = Block(171, COLOR_LIME)
CARPET_PINK = Block(171, COLOR_PINK)
CARPET_GRAY = Block(171, COLOR_GRAY)
CARPET_LIGHT_GRAY = Block(171, COLOR_LIGHT_GRAY)
CARPET_CYAN = Block(171, COLOR_CYAN)
CARPET_PURPLE = Block(171, COLOR_PURPLE)
CARPET_BLUE = Block(171, COLOR_BLUE)
CARPET_BROWN = Block(171, COLOR_BROWN)
CARPET_GREEN = Block(171, COLOR_GREEN)
CARPET_RED = Block(171, COLOR_RED)
CARPET_BLACK = Block(171, COLOR_BLACK)
HARDENED_CLAY = Block(172)
COAL_BLOCK = Block(173)
PACKED_ICE = Block(174)
DOUBLE_PLANT_SUNFLOWER = Block(175)
DOUBLE_PLANT_LILAC = Block(175, 1)
DOUBLE_PLANT_TALLGRASS = Block(175, 2)
DOUBLE_PLANT_LARGE_FERN = Block(175, 3)
DOUBLE_PLANT_ROSE_BUSH = Block(175, 4)
DOUBLE_PLANT_PEONY = Block(175, 5)
STANDING_BANNER = Block(176)
WALL_BANNER = Block(177)
DAYLIGHT_DETECTOR_INVERTED = Block(178)
RED_SANDSTONE = Block(179)
RED_SANDSTONE_CHISELED = Block(179, 1)
RED_SANDSTONE_SMOOTH = Block(179, 2)
RED_SANDSTONE_STAIRS = Block(180)
DOUBLE_STONE_SLAB_2 = Block(181)
STONE_SLAB_2 = Block(182)
SPRUCE_FENCE_GATE = Block(183)
BIRCH_FENCE_GATE = Block(184)
JUNGLE_FENCE_GATE = Block(185)
DARK_OAK_FENCE_GATE = Block(186)
ACACIA_FENCE_GATE = Block(187)
SPRUCE_FENCE = Block(188)
BIRCH_FENCE = Block(189)
JUNGLE_FENCE = Block(190)
DARK_OAK_FENCE = Block(191)
ACACIA_FENCE = Block(192)
SPRUCE_DOOR_BLOCK = Block(193)
BIRCH_DOOR_BLOCK = Block(194)
JUNGLE_DOOR_BLOCK = Block(195)
ACACIA_DOOR_BLOCK = Block(196)
DARK_OAK_DOOR_BLOCK = Block(197)
END_ROD = Block(198)
CHORUS_PLANT = Block(199)
CHORUS_FLOWER = Block(200)
PURPUR_BLOCK = Block(201)
PURPUR_PILLAR = Block(202)
PURPUR_STAIRS = Block(203)
PURPUR_DOUBLE_SLAB = Block(204)
PURPUR_SLAB = Block(205)
END_BRICKS = Block(206)
BEETROOTS = Block(207)
GRASS_PATH = Block(208)
END_GATEWAY = Block(209)
REPEATING_COMMAND_BLOCK = Block(210)
CHAIN_COMMAND_BLOCK = Block(211)
FROSTED_ICE = Block(212)
MAGMA = Block(213)
NETHER_WART_BLOCK = Block(214)
RED_NETHER_BRICK = Block(215)
BONE_BLOCK = Block(216)
STRUCTURE_VOID = Block(217)
OBSERVER = Block(218)
SHULKER_BOX_WHITE = Block(219)
SHULKER_BOX_ORANGE = Block(220)
SHULKER_BOX_MAGENTA = Block(221)
SHULKER_BOX_LIGHT_BLUE = Block(222)
SHULKER_BOX_YELLOW = Block(223)
SHULKER_BOX_LIME = Block(224)
SHULKER_BOX_PINK = Block(225)
SHULKER_BOX_GRAY = Block(226)
SHULKER_BOX_SILVER = Block(227)
SHULKER_BOX_CYAN = Block(228)
SHULKER_BOX_PURPLE = Block(229)
SHULKER_BOX_BLUE = Block(230)
SHULKER_BOX_BROWN = Block(231)
SHULKER_BOX_GREEN = Block(232)
SHULKER_BOX_RED = Block(233)
SHULKER_BOX_BLACK = Block(234)
GLAZED_TERACOTA_WHITE = Block(235)
GLAZED_TERACOTA_ORANGE = Block(236)
GLAZED_TERACOTA_MAGENTA = Block(237)
GLAZED_TERACOTA_LIGHT_BLUE = Block(238)
GLAZED_TERACOTA_YELLOW = Block(239)
GLAZED_TERACOTA_LIME = Block(240)
GLAZED_TERACOTA_PINK = Block(241)
GLAZED_TERACOTA_GRAY = Block(242)
GLAZED_TERACOTA_LIGHT_GRAY = Block(243)
GLAZED_TERACOTA_CYAN = Block(244)
GLAZED_TERACOTA_PURPLE = Block(245)
GLAZED_TERACOTA_BLUE = Block(246)
GLAZED_TERACOTA_BROWN = Block(247)
GLAZED_TERACOTA_GREEN = Block(248)
GLAZED_TERACOTA_RED = Block(249)
GLAZED_TERACOTA_BLACK = Block(250)
CONCRETE_WHITE = Block(251, COLOR_WHITE)
CONCRETE_ORANGE = Block(251, COLOR_ORANGE)
CONCRETE_MAGENTA = Block(251, COLOR_MAGENTA)
CONCRETE_LIGHT_BLUE = Block(251, COLOR_LIGHT_BLUE)
CONCRETE_YELLOW = Block(251, COLOR_YELLOW)
CONCRETE_LIME = Block(251, COLOR_LIME)
CONCRETE_PINK = Block(251, COLOR_PINK)
CONCRETE_GRAY = Block(251, COLOR_GRAY)
CONCRETE_LIGHT_GRAY = Block(251, COLOR_LIGHT_GRAY)
CONCRETE_CYAN = Block(251, COLOR_CYAN)
CONCRETE_PURPLE = Block(251, COLOR_PURPLE)
CONCRETE_BLUE = Block(251, COLOR_BLUE)
CONCRETE_BROWN = Block(251, COLOR_BROWN)
CONCRETE_GREEN = Block(251, COLOR_GREEN)
CONCRETE_RED = Block(251, COLOR_RED)
CONCRETE_BLACK = Block(251, COLOR_BLACK)
CONCRETE_POWDER_WHITE = Block(252, COLOR_WHITE)
CONCRETE_POWDER_ORANGE = Block(252, COLOR_ORANGE)
CONCRETE_POWDER_MAGENTA = Block(252, COLOR_MAGENTA)
CONCRETE_POWDER_LIGHT_BLUE = Block(252, COLOR_LIGHT_BLUE)
CONCRETE_POWDER_YELLOW = Block(252, COLOR_YELLOW)
CONCRETE_POWDER_LIME = Block(252, COLOR_LIME)
CONCRETE_POWDER_PINK = Block(252, COLOR_PINK)
CONCRETE_POWDER_GRAY = Block(252, COLOR_GRAY)
CONCRETE_POWDER_LIGHT_GRAY = Block(252, COLOR_LIGHT_GRAY)
CONCRETE_POWDER_CYAN = Block(252, COLOR_CYAN)
CONCRETE_POWDER_PURPLE = Block(252, COLOR_PURPLE)
CONCRETE_POWDER_BLUE = Block(252, COLOR_BLUE)
CONCRETE_POWDER_BROWN = Block(252, COLOR_BROWN)
CONCRETE_POWDER_GREEN = Block(252, COLOR_GREEN)
CONCRETE_POWDER_RED = Block(252, COLOR_RED)
CONCRETE_POWDER_BLACK = Block(252, COLOR_BLACK)
STRUCTURE_BLOCK = Block(255)
IRON_SHOVEL = Block(256)
IRON_PICKAXE = Block(257)
IRON_AXE = Block(258)
FLINT_AND_STEEL = Block(259)
APPLE = Block(260)
BOW = Block(261)
ARROW = Block(262)
COAL = Block(263)
COAL_CHARCOAR = Block(263, 1)
DIAMOND = Block(264)
IRON_INGOT = Block(265)
GOLD_INGOT = Block(266)
IRON_SWORD = Block(267)
WOODEN_SWORD = Block(268)
WOODEN_SHOVEL = Block(269)
WOODEN_PICKAXE = Block(270)
WOODEN_AXE = Block(271)
STONE_SWORD = Block(272)
STONE_SHOVEL = Block(273)
STONE_PICKAXE = Block(274)
STONE_AXE = Block(275)
DIAMOND_SWORD = Block(276)
DIAMOND_SHOVEL = Block(277)
DIAMOND_PICKAXE = Block(278)
DIAMOND_AXE = Block(279)
STICK = Block(280)
BOWL = Block(281)
MUSHROOM_STEW = Block(282)
GOLDEN_SWORD = Block(283)
GOLDEN_SHOVEL = Block(284)
GOLDEN_PICKAXE = Block(285)
GOLDEN_AXE = Block(286)
STRING = Block(287)
FEATHER = Block(288)
GUNPOWDER = Block(289)
WOODEN_HOE = Block(290)
STONE_HOE = Block(291)
IRON_HOE = Block(292)
DIAMOND_HOE = Block(293)
GOLDEN_HOE = Block(294)
WHEAT_SEEDS = Block(295)
WHEAT = Block(296)
BREAD = Block(297)
LEATHER_HELMET = Block(298)
LEATHER_CHESTPLATE = Block(299)
LEATHER_LEGGINGS = Block(300)
LEATHER_BOOTS = Block(301)
CHAINMAIL_HELMET = Block(302)
CHAINMAIL_CHESTPLATE = Block(303)
CHAINMAIL_LEGGINGS = Block(304)
CHAINMAIL_BOOTS = Block(305)
IRON_HELMET = Block(306)
IRON_CHESTPLATE = Block(307)
IRON_LEGGINGS = Block(308)
IRON_BOOTS = Block(309)
DIAMOND_HELMET = Block(310)
DIAMOND_CHESTPLATE = Block(311)
DIAMOND_LEGGINGS = Block(312)
DIAMOND_BOOTS = Block(313)
GOLDEN_HELMET = Block(314)
GOLDEN_CHESTPLATE = Block(315)
GOLDEN_LEGGINGS = Block(316)
GOLDEN_BOOTS = Block(317)
FLINT = Block(318)
PORKCHOP = Block(319)
COOKED_PORKCHOP = Block(320)
PAINTING = Block(321)
GOLDEN_APPLE = Block(322)
GOLDEN_APPLE_ENCHANTED = Block(322, 1)
SIGN = Block(323)
WOODEN_DOOR_OAK = Block(324)
BUCKET = Block(325)
WATER_BUCKET = Block(326)
LAVA_BUCKET = Block(327)
MINECART = Block(328)
SADDLE = Block(329)
IRON_DOOR = Block(330)
REDSTONE = Block(331)
SNOWBALL = Block(332)
BOAT = Block(333)
LEATHER = Block(334)
MILK_BUCKET = Block(335)
BRICK = Block(336)
CLAY_BALL = Block(337)
REEDS_SUGAR_CANES = Block(338)
PAPER = Block(339)
BOOK = Block(340)
SLIME_BALL = Block(341)
CHEST_MINECART = Block(342)
FURNACE_MINECART = Block(343)
EGG = Block(344)
COMPASS = Block(345)
FISHING_ROD = Block(346)
CLOCK = Block(347)
GLOWSTONE_DUST = Block(348)
FISH_RAW = Block(349)
FISH_RAW_SALMON = Block(349, 1)
FISH_CLOWNFISH = Block(349, 2)
FISH_PUFFERFISH = Block(349, 3)
COOKED_FISH = Block(350)
COOKED_FISH_SALMON = Block(350, 1)
DYE_INK_SACK = Block(351)
DYE_ROSE_RED = Block(351, 1)
DYE_CACTUS_GREEN = Block(351, 2)
DYE_COCO_BEANS = Block(351, 3)
DYE_LAPIS_LAZULI = Block(351, 4)
DYE_PURPLE = Block(351, 5)
DYE_CYAN = Block(351, 6)
DYE_LIGHT_GRAY = Block(351, 7)
DYE_GRAY = Block(351, 8)
DYE_PINK = Block(351, 9)
DYE_LIME = Block(351, 10)
DYE_DANDELION_YELLOW = Block(351, 11)
DYE_LIGHT_BLUE = Block(351, 12)
DYE_MAGENTA = Block(351, 13)
DYE_ORANGE = Block(351, 14)
DYE_BONE_MEAL = Block(351, 15)
BONE = Block(352)
SUGAR = Block(353)
CAKE = Block(354)
BED_2 = Block(355)
REPEATER = Block(356)
COOKIE = Block(357)
FILLED_MAP = Block(358)
SHEARS = Block(359)
MELON = Block(360)
PUMPKIN_SEEDS = Block(361)
MELON_SEEDS = Block(362)
BEEF = Block(363)
COOKED_BEEF = Block(364)
CHICKEN = Block(365)
COOKED_CHICKEN = Block(366)
ROTTEN_FLESH = Block(367)
ENDER_PEARL = Block(368)
BLAZE_ROD = Block(369)
GHAST_TEAR = Block(370)
GOLD_NUGGET = Block(371)
NETHER_WART_2 = Block(372)
POTION = Block(373)
GLASS_BOTTLE = Block(374)
SPIDER_EYE = Block(375)
FERMENTED_SPIDER_EYE = Block(376)
BLAZE_POWDER = Block(377)
MAGMA_CREAM = Block(378)
BREWING_STAND_2 = Block(379)
CAULDRON_2 = Block(380)
ENDER_EYE = Block(381)
SPECKLED_MELON = Block(382)
SPAWN_EGG_ELDER_GUARDIAN = Block(383, 4)
SPAWN_EGG_WITHER_SKELETON = Block(383, 5)
SPAWN_EGG_STRAY = Block(383, 6)
SPAWN_EGG_HUSK = Block(383, 23)
SPAWN_EGG_ZOMBIE_VILLAGER = Block(383, 27)
SPAWN_EGG_SKELETON_HORSE = Block(383, 28)
SPAWN_EGG_ZOMBIE_HORSE = Block(383, 29)
SPAWN_EGG_DONKEY = Block(383, 31)
SPAWN_EGG_MULE = Block(383, 32)
SPAWN_EGG_EVOKER = Block(383, 34)
SPAWN_EGG_VEX = Block(383, 35)
SPAWN_EGG_VINDICATOR = Block(383, 36)
SPAWN_EGG_CREEPER = Block(383, 50)
SPAWN_EGG_SKELETON = Block(383, 51)
SPAWN_EGG_SPIDER = Block(383, 52)
SPAWN_EGG_ZOMBIE = Block(383, 54)
SPAWN_EGG_SLIME = Block(383, 55)
SPAWN_EGG_GHAST = Block(383, 56)
SPAWN_EGG_ZOMBIE_PIGMAN = Block(383, 57)
SPAWN_EGG_ENDERMAN = Block(383, 58)
SPAWN_EGG_CAVE_SPIDER = Block(383, 59)
SPAWN_EGG_SILVERFISH = Block(383, 60)
SPAWN_EGG_BLAZE = Block(383, 61)
SPAWN_EGG_MAGMA_CUBE = Block(383, 62)
SPAWN_EGG_BAT = Block(383, 65)
SPAWN_EGG_WITCH = Block(383, 66)
SPAWN_EGG_ENDERMITE = Block(383, 67)
SPAWN_EGG_GUARDIAN = Block(383, 68)
SPAWN_EGG_SHULKER = Block(383, 69)
SPAWN_EGG_PIG = Block(383, 90)
SPAWN_EGG_SHEEP = Block(383, 91)
SPAWN_EGG_COW = Block(383, 92)
SPAWN_EGG_CHICKEN = Block(383, 93)
SPAWN_EGG_SQUID = Block(383, 94)
SPAWN_EGG_WOLF = Block(383, 95)
SPAWN_EGG_MOOSHROOM = Block(383, 96)
SPAWN_EGG_OCELOT = Block(383, 98)
SPAWN_EGG_HORSE = Block(383, 100)
SPAWN_EGG_RABBIT = Block(383, 101)
SPAWN_EGG_POLAR_BEAR = Block(383, 102)
SPAWN_EGG_LLAMA = Block(383, 103)
SPAWN_EGG_PARROT = Block(383, 105)
SPAWN_EGG_VILLAGER = Block(383, 120)
EXPERIENCE_BOTTLE = Block(384)
FIRE_CHARGE = Block(385)
WRITABLE_BOOK = Block(386)
WRITTEN_BOOK = Block(387)
EMERALD = Block(388)
ITEM_FRAME = Block(389)
FLOWER_POT_2 = Block(390)
CARROT = Block(391)
POTATO = Block(392)
BAKED_POTATO = Block(393)
POISONOUS_POTATO = Block(394)
MAP = Block(395)
GOLDEN_CARROT = Block(396)
SKULL_SKELETON = Block(397)
SKULL_WITHER_SKELETON = Block(397, 1)
SKULL_ZOMBIE = Block(397, 2)
SKULL_HUMAN = Block(397, 3)
SKULL_CREEPER = Block(397, 4)
SKULL_DRAGON = Block(397, 5)
CARROT_ON_A_STICK = Block(398)
NETHER_STAR = Block(399)
PUMPKIN_PIE = Block(400)
FIREWORKS = Block(401)
FIREWORK_CHARGE = Block(402)
ENCHANTED_BOOK = Block(403)
COMPARATOR = Block(404)
NETHERBRICK = Block(405)
QUARTZ = Block(406)
TNT_MINECART = Block(407)
HOPPER_MINECART = Block(408)
PRISMARINE_SHARD = Block(409)
PRISMARINE_CRYSTALS = Block(410)
RABBIT = Block(411)
COOKED_RABBIT = Block(412)
RABBIT_STEW = Block(413)
RABBIT_FOOT = Block(414)
RABBIT_HIDE = Block(415)
ARMOR_STAND = Block(416)
IRON_HORSE_ARMOR = Block(417)
GOLDEN_HORSE_ARMOR = Block(418)
DIAMOND_HORSE_ARMOR = Block(419)
LEAD = Block(420)
NAME_TAG = Block(421)
COMMAND_BLOCK_MINECART = Block(422)
MUTTON = Block(423)
COOKED_MUTTON = Block(424)
BANNER = Block(425)
END_CRYSTAL = Block(426)
SPRUCE_DOOR = Block(427)
BIRCH_DOOR = Block(428)
JUNGLE_DOOR = Block(429)
ACACIA_DOOR = Block(430)
DARK_OAK_DOOR = Block(431)
CHORUS_FRUIT = Block(432)
POPPED_CHORUS_FRUIT = Block(433)
BEETROOT = Block(434)
BEETROOT_SEEDS = Block(435)
BEETROOT_SOUP = Block(436)
DRAGON_BREATH = Block(437)
SPLASH_POTION = Block(438)
SPECTRAL_ARROW = Block(439)
TIPPED_ARROW = Block(440)
LINGERING_POTION = Block(441)
SHIELD = Block(442)
ELYTRA = Block(443)
SPRUCE_BOAT = Block(444)
BIRCH_BOAT = Block(445)
JUNGLE_BOAT = Block(446)
ACACIA_BOAT = Block(447)
DARK_OAK_BOAT = Block(448)
TOTEM_OF_UNDYING = Block(449)
SHULKER_SHELL = Block(450)
IRON_NUGGET = Block(452)
KNOWLEDGE_BOOK = Block(453)
RECORD_13 = Block(2256)
RECORD_CAT = Block(2257)
RECORD_BLOCKS = Block(2258)
RECORD_CHIRP = Block(2259)
RECORD_FAR = Block(2260)
RECORD_MALL = Block(2261)
RECORD_MELLOHI = Block(2262)
RECORD_STAL = Block(2263)
RECORD_STRAD = Block(2264)
RECORD_WARD = Block(2265)
RECORD_11 = Block(2266)
RECORD_WAIT = Block(2267)

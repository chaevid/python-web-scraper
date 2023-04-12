player = {
    'name': 'chaevid',
    'age': 31,
    'live': True,
    'fav_foods': ['🍗', '🍔', '🍕'],
}
print(player)
print(player.pop('age'))
print(player)
player['xp'] = 1500
player['fav_foods'].append('🍟')
print(player)
# print(player.get('fav_foods'))

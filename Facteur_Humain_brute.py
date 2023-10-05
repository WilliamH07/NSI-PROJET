# Initialization
People = ['Mike', 'Harvey', 'Louis', 'Logan', 'Rachel', 'Donna', 'Katrina', 'Sheila']

# Preferences
Preferences = {
    'Mike':   ['Rachel', 'Katrina', 'Donna', 'Sheila'],
    'Harvey': ['Donna', 'Katrina', 'Rachel', 'Sheila'],
    'Louis':  ['Sheila', 'Donna', 'Katrina', 'Rachel'],
    'Logan':  ['Rachel', 'Katrina', 'Donna', 'Sheila'],
    'Rachel':  ['Mike', 'Logan', 'Harvey', 'Louis'],
    'Donna':   ['Harvey', 'Louis', 'Mike', 'Logan'],
    'Katrina': ['Mike', 'Harvey', 'Louis', 'Logan'],
    'Sheila':  ['Louis', 'Logan', 'Harvey', 'Mike']
}

def main():
    People_Free = list(People)

    # Part 3: Proposal
    Matches = {person: '' for person in People}
    
    while len(People_Free) > 0:
        for person in People_Free:
            for partner in Preferences[person]:
                current_partner = Matches[partner]
                if current_partner == '':
                    Matches[partner] = person
                    People_Free.remove(person)
                    print('{} is no longer a free person and is tentatively engaged to {} !'.format(person, partner))
                    break
                else:
                    preference_list = Preferences[partner]
                    if preference_list.index(person) < preference_list.index(current_partner):
                        Matches[partner] = person
                        People_Free.remove(person)
                        People_Free.append(current_partner)
                        print('{} was earlier engaged to {} but now is engaged to {}! '.format(partner, current_partner, person))
                        break

    print('\n')
    print('Stable Matching Finished ! Happy engagement !')
    for person, partner in Matches.items():
        print('{} is engaged to {} !'.format(person, partner))

if __name__ == "__main__":
    main()

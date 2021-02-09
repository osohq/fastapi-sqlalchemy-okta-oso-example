allow(user: User, "create", _: BearBase) if
    not user.is_banned;

allow(_: User, "index", _: User);

allow(user: User, "index", bear: Bear) if
    bear.owner = user or
    bear.species = Species.polar;

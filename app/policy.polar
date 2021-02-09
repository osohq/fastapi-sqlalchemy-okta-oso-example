allow(user: User, "create", _: BearBase) if
    not user.is_banned;

allow(_: User, "index", _: User);

allow(_: User, "index", _: Bear);

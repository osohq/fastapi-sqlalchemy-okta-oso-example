allow(user: User, "create", _: BearBase) if
    not user.is_banned;

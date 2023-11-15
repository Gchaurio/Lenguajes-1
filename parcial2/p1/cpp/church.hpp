struct Church {
  enum Type {
    Cero,
    Suc
  };

  Type type;

  Church() : type(Cero) {}
  Church(const Church& other) : type(other.type) {}

  explicit Church(Type type) : type(type) {}
};

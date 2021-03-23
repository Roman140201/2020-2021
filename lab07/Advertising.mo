model Advertising

parameter Real N = 1940; // максимальное количество людей, которых может заинтересовать товар
parameter Real n0 = 26; // количество людей, знающих о товаре в начальный момент времени
Real n(start=n0); // количество людей, знающих о товаре

function k
  input Real t;
  output Real result;
algorithm
//result := 0.91; //для первого случая
//result := 0.00001; //для второго случая
  result := 0.18*t; //для третьего случая
end k;

function p
  input Real t;
  output Real result;
algorithm
//result := 0.00005; // для первого случая
//result := 0.81; //для второго случая
  result := 0.31*t; //для третьего случая
end p;

equation

der(n) = (k(time) + p(time) * n)*(N-n);

end Advertising;

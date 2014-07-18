rubby issue
===

那些奇怪的语法
---

数组切片
---

    >> a = [1,2,3,4]
    => [1, 2, 3, 4]
    >> a[4]
    => nil
    >> a[0,1]
    => [1]
    >> a[0..1]
    => [1, 2]
    >> a[0...1]
    => [1]
    >> a[0,0]
    => []
    >> a[3,0]
    => []
    >> a[3,4]
    => [4]
    >> a[2,10]
    => [3, 4]
    >> a[4]   # 这一行+下几行会非常奇怪
    => nil
    >> a[4,10]
    => []     # a[4]明明已经nil了，居然还是[]
    >> a[5]
    => nil    # a[5]是nil,可和a[4]不同得到的是nil
    >> a[5,10]
    => nil

hash(dict)默认值
---

    >> d = Hash.new([])
    => {}
    >> d[:one] << 'a'
    => ["a"]
    >> d[:two] << 'b'
    => ["a", "b"]
    >> d[:one]
    => ["a", "b"]
    >> d[:three]
    => ["a", "b"]

需要这样避免

    hash = Hash.new {|hash, key| hash[key] = [] }
    hash[:one] << "uno"
    hash[:two] << "dos"

    assert_equal ['uno'], hash[:one]
    assert_equal ['dos'], hash[:two]
    assert_equal [], hash[:three]
